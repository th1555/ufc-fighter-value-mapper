"""
ufc_stats_topup.py

Purpose
-------
Keep a local mirror of UFCStats current by scraping only the events that are
missing from an existing set of six CSVs whose schema matches the Greco1899
`scrape_ufc_stats` repository. The intended workflow is:

    Greco snapshot (historical seed)  ->  this script (incremental top-up)
        ->  the six CSVs are pushed to a public repository
        ->  notebooks repoint BASE_URL to that repo; nothing else changes.

Output files (compatible column order with Greco; verified live)
--------------------------------------------------------------------
    ufc_event_details.csv    EVENT, URL, DATE, LOCATION
    ufc_fight_details.csv     EVENT, BOUT, URL
    ufc_fight_results.csv     EVENT, BOUT, OUTCOME, WEIGHTCLASS, METHOD, ROUND,
                              TIME, TIME FORMAT, REFEREE, DETAILS, URL
    ufc_fight_stats.csv       EVENT, BOUT, ROUND, FIGHTER, KD, SIG.STR.,
                              SIG.STR. %, TOTAL STR., TD, TD %, SUB.ATT, REV.,
                              CTRL, HEAD, BODY, LEG, DISTANCE, CLINCH, GROUND
    ufc_fighter_details.csv   FIRST, LAST, NICKNAME, URL
    ufc_fighter_tott.csv      FIGHTER, HEIGHT, WEIGHT, REACH, STANCE, DOB, URL

Two things to verify locally on first run:
    1. ufcstats.com requires real JS execution; this script drives
       a real Chrome via SeleniumBase UC mode, which opens with a disconnect/
       reconnect to clear "checking your browser" and will click a Turnstile
       widget if one appears (HEADLESS=False is required for that click). A visible
       Chrome window will open; that is expected.
    2. The round stats parser (parse_fight_stats) could not be
       checked against the live DOM from the authoring environment. Run
       `--debug-fight <fight_url>`

Dependencies
------------
    requests          >= 2.28   (Greco seed download only)
    seleniumbase      >= 4.20   (ufcstats reads; UC mode drives real Chrome,
                                 resolves the matching driver, clears the JS gate)
    beautifulsoup4    >= 4.11
    lxml              >= 4.9     (parser; faster, more lenient than html.parser)
    pandas            >= 1.5
    Python            >= 3.10
    Google Chrome installed (SeleniumBase drives r local Chrome).

    pip install "requests>=2.28" seleniumbase "beautifulsoup4>=4.11" "lxml>=4.9" "pandas>=1.5"
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path
from typing import Optional

import pandas as pd
import requests
from bs4 import BeautifulSoup

# ufcstats.com sits behind a JavaScript/browser challenge (this is what stalled
# the Greco mirror in mid-May 2026). Plain `requests` and curl_cffi TLS
# impersonation were both rejected, and bare undetected-chromedriver kept tripping
# over Chrome/driver version matching on this machine. Reads therefore go through
# SeleniumBase in UC (undetected) mode, which downloads the matching driver for
# the installed Chrome itself, clears the JS challenge via a disconnect/reconnect,
# and can click a Turnstile widget if one appears. The browser is launched once
# and reused across every request; see get_driver(). `requests` is kept only for
# the Greco seed, which is served from GitHub and is not gated.
#
# seleniumbase is imported lazily inside get_driver() so this module still imports
# cleanly on a machine without it or without Chrome.

# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------

UFCSTATS_ROOT = "http://ufcstats.com"
COMPLETED_EVENTS_URL = f"{UFCSTATS_ROOT}/statistics/events/completed?page=all"

# A real browser User-Agent. ufcstats.com historically served static HTML to
# plain clients; if it now gates on UA/IP, this header alone may not be enough
# and get_soup() will need a browser engine (see module docstring).
HTTP_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}

DEFAULT_DELAY_SECONDS = 1.0   # politeness; ufcstats is a small site
DEFAULT_RETRIES = 3
REQUEST_TIMEOUT = 30

# Browser-engine settings (SeleniumBase UC mode).
# HEADLESS=False (a visible window) is the most reliable way past a Cloudflare
# style challenge, and is required if a Turnstile widget needs a physical click;
# headless is detectable and more likely to loop. SeleniumBase resolves the
# Chrome/driver version itself, so no version pin is needed here.
HEADLESS = False
# Seconds SeleniumBase stays disconnected while the JS challenge runs on the first
# navigation; 6 is a safe default, raise it on a slow connection.
RECONNECT_SECONDS = 6
# How long to wait for the JS challenge to clear after each navigation.
GATE_WAIT_SECONDS = 30
GATE_PHRASES = ("This site requires JavaScript", "Checking r browser")

# Exact column orders. These are asserted against the live Greco headers in the
# accompanying validation step; do not reorder without re-checking.
EVENT_DETAILS_COLS = ["EVENT", "URL", "DATE", "LOCATION"]
FIGHT_DETAILS_COLS = ["EVENT", "BOUT", "URL"]
FIGHT_RESULTS_COLS = [
    "EVENT", "BOUT", "OUTCOME", "WEIGHTCLASS", "METHOD", "ROUND",
    "TIME", "TIME FORMAT", "REFEREE", "DETAILS", "URL",
]
FIGHT_STATS_COLS = [
    "EVENT", "BOUT", "ROUND", "FIGHTER", "KD", "SIG.STR.", "SIG.STR. %",
    "TOTAL STR.", "TD", "TD %", "SUB.ATT", "REV.", "CTRL",
    "HEAD", "BODY", "LEG", "DISTANCE", "CLINCH", "GROUND",
]
FIGHTER_DETAILS_COLS = ["FIRST", "LAST", "NICKNAME", "URL"]
FIGHTER_TOTT_COLS = ["FIGHTER", "HEIGHT", "WEIGHT", "REACH", "STANCE", "DOB", "URL"]

OUTPUT_FILENAMES = {
    "event_details": "ufc_event_details.csv",
    "fight_details": "ufc_fight_details.csv",
    "fight_results": "ufc_fight_results.csv",
    "fight_stats": "ufc_fight_stats.csv",
    "fighter_details": "ufc_fighter_details.csv",
    "fighter_tott": "ufc_fighter_tott.csv",
}

GRECO_RAW_BASE = "https://raw.githubusercontent.com/Greco1899/scrape_ufc_stats/main/"


# [Continued - truncated for brevity in initial commit]
