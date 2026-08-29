"""
UFC Fighter Value Map: interactive dashboard.

Reads the frozen pipeline outputs (parquets) and presents the two-axis map, a
per-fighter detail view, and the booking-model under-booked ranking. Run with:

    streamlit run app.py

Data files expected in the ./data folder:
    public_profile_axis.parquet        the public-profile axis (three-signal, rebuilt)
    glicko_current_continuous.parquet  the competitive axis (Glicko rating, tier)
    style_clusters.parquet             GMM style archetype per fighter
    booking_residuals.parquet          booking-propensity model output
    fighter_divisions.parquet          primary division, divisions, recent form
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# [App code continues - content truncated for brevity in display]
