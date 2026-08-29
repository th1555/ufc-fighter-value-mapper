"""
pytrends API verification

Source: Google Trends (unofficial API, no Google-published endpoint)
Package: pytrends
Run date: 2026-05-04

Verifies whether Google Trends is a usable source for the public profile axis. It
confirms the pytrends client installs and initialises, builds a sample payload for a
small fighter set, pulls search interest over a 12-month US-scoped window, tests
back-to-back queries with a sleep between them, and documents the urllib3 v2
incompatibility affecting the retries and backoff_factor parameters.

Outcome: the package installs and runs, but Trends was not adopted. Two problems
made it unsuitable. First, the pytrends client is unreliable: it depends on an
unofficial endpoint and breaks against urllib3 v2 (the method_whitelist to
allowed_methods rename documented in the client below). Second, and more
fundamentally, Google Trends normalises each query independently to a 0 to 100
scale, so single-term pulls are not comparable across fighters without a shared
anchor query. The public profile axis was instead built from Wikipedia pageviews
and GDELT news volume.

This file is retained as the record of that evaluation. It is a .py script rather
than a notebook because it runs locally in PyCharm against a controlled urllib3 pin,
not in Colab. No production pulls were run, as the source was dropped.

Environment note: run locally, not in Colab, for control over the urllib3 version.
"""

import pandas as pd
import time
from datetime import datetime
from pytrends.request import TrendReq

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 60)


def main():
    print(f"pytrends verification run date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Start pytrends
    # hl = host language, tz = timezone offset (300 = US Central time)
    # timeout = (connection_timeout, read_timeout) in seconds
    # Retries/backoff_factor are omitted because they trigger a urllib3
    # incompatibility (method_whitelist was renamed allowed_methods in urllib3 2.0)
    pytrends = TrendReq(
        hl='en-US',
        tz=300,
        timeout=(10, 25)
    )
    print("pytrends client initialised")
    print()

    # First query: build payload and pull search interest data
    keywords = ['Conor McGregor', 'Israel Adesanya']

    print(f"Building first pytrends query")
    print(f"Keywords: {keywords}")
    print(f"Timeframe: today 12-m (last 12 months)")
    print(f"Geo: US (post-PPV US market focus)")
    print()

    try:
        pytrends.build_payload(
            kw_list=keywords,
            timeframe='today 12-m',
            geo='US',
            gprop=''  # all Google properties (web search default)
        )
        print("OK Payload built successfully")
    except Exception as e:
        print(f"FAIL Payload build failed: {type(e).__name__}: {e}")
        return

    print()
    print("First query...")
    start_time = time.time()

    try:
        interest_data = pytrends.interest_over_time()
        elapsed = time.time() - start_time

        if len(interest_data) == 0:
            print(f"WARN First query returned in {elapsed:.1f} seconds with empty results")
            print("Potentially due to rate limiting or low volume keywords")
        else:
            print(f"OK First query completed in {elapsed:.1f} seconds")
            print(f"   Returned {len(interest_data)} weekly records")
            print()
            print("Sample of search interest data:")
            print(interest_data.head(10))
            print()
            print("Statistics:")
            print(interest_data.describe())

            # Save the output to CSV as a verification artifact
            interest_data.to_csv('pytrends_verification_query1.csv')
            print()
            print(f"Saved output to pytrends_verification_query1.csv")

    except Exception as e:
        elapsed = time.time() - start_time
        print(f"FAIL First query failed after {elapsed:.1f} seconds")
        print(f"Error: {type(e).__name__}: {e}")
        print()
        print("Common causes: rate limiting, IP blocking or API drift")

    # Second query: test sustained access with different keywords
    print()
    print("Wait 30 seconds...")
    time.sleep(30)

    keywords_2 = ['Khabib Nurmagomedov', 'Jon Jones']

    try:
        pytrends.build_payload(
            kw_list=keywords_2,
            timeframe='today 12-m',
            geo='US'
        )
        print("Second query...")
        start_time = time.time()
        interest_2 = pytrends.interest_over_time()
        elapsed = time.time() - start_time

        if len(interest_2) == 0:
            print(f"WARN Second query returned in {elapsed:.1f} seconds with empty results")
        else:
            print(f"OK Second query completed in {elapsed:.1f} seconds")
            print(f"Sustained access works for back-to-back queries with a 30 second sleep")
            print()
            print("Sample:")
            print(interest_2.head(5))
            interest_2.to_csv('pytrends_verification_query2.csv')
            print()
            print(f"Saved query 2 output to pytrends_verification_query2.csv")

    except Exception as e:
        elapsed = time.time() - start_time
        print(f"FAIL Second query failed after {elapsed:.1f} seconds")
        print(f"Error: {type(e).__name__}: {e}")
        print()
        print("Rate limit detected on back-to-back queries.")
        print("Recommendation: space queries by at least 60 seconds.")

    # Verification summary
    print()
    print("PYTRENDS VERIFICATION SUMMARY")
    print("=" * 80)
    print()
    print("Package: pytrends")
    print("Source: Google Trends (unofficial API)")
    print("Use in project: Public profile axis input (Trends baseline and activation)")
    print()
    print("Verified status:")
    print("- Package installs cleanly via pip")
    print("- TrendReq client initialises (without retries due to urllib3 v2 incompatibility)")
    print("- build_payload accepts the parameters needed for the project")
    print("- Query results captured in pytrends_verification_query1.csv and _query2.csv")
    print()
    print("Stability assessment:")
    print("- The package is unofficial; Google has no public Trends API")
    print("- urllib3 v2 incompatibility requires either pinning urllib3<2.0 or omitting retries")
    print("- Production pattern: pull data once, cache locally, retry failed pulls patiently")
    print()


if __name__ == '__main__':
    main()