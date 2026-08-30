
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
 
# ----------------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------------
st.set_page_config(page_title="UFC Fighter Value Map", layout="wide")
 
# Data location. Locally, read the live pipeline outputs straight from the Google
# Drive mount, so the dashboard always reflects the current parquets and needs no
# manual copy. When that folder is absent (for example on Streamlit Cloud, where the
# parquets are bundled in the repo), fall back to a local ./data folder. Same code,
# both places.
LIVE_DATA = Path(r"G:\My Drive\Masters in Artificial Intelligence Applied to Sport\Masters Final Project\Pugnator mapper valorem\EDA\Code Outputs")
DATA = LIVE_DATA if LIVE_DATA.exists() else Path(__file__).parent / "data"
FREEZE = "2026-07-11"                    # data freeze date, for the footer
 
REQUIRED = [
    "public_profile_axis.parquet",
    "glicko_current_continuous.parquet",
    "style_clusters.parquet",
    "booking_residuals.parquet",
    "fighter_divisions.parquet",
]
missing = [f for f in REQUIRED if not (DATA / f).exists()]
if missing:
    st.error(
        "Missing data files in the ./data folder:\n\n"
        + "\n".join(f"- {m}" for m in missing)
        + "\n\nCopy the parquet outputs into a folder named 'data' next to app.py."
    )
    st.stop()
 
 
# ----------------------------------------------------------------------------
# Data loading
#
# One function that reads every parquet and joins them into a single table, one
# row per fighter. Wrapped in st.cache_data so it runs once and is reused on
# every interaction rather than re-read each time a filter changes.
# ----------------------------------------------------------------------------
@st.cache_data
def load_fighters():
    prof = pd.read_parquet(DATA / "public_profile_axis.parquet")
    glk = pd.read_parquet(DATA / "glicko_current_continuous.parquet")[
        ["FIGHTER", "RATING", "TIER", "N_FIGHTS", "LAST_FIGHT"]
    ]
    sty = pd.read_parquet(DATA / "style_clusters.parquet")[
        ["FIGHTER", "primary_style", "style_confidence"]
    ]
    # primary_division, last_division, divs (list), recent_form, wc
    divs = pd.read_parquet(DATA / "fighter_divisions.parquet")
    # the booking model only scored the 439-fighter modelling population; a left
    # join leaves the rest with NaN residuals, which we treat as "not scored".
    res = pd.read_parquet(DATA / "booking_residuals.parquet")[
        ["FIGHTER", "pred", "residual", "headlined", "main_events"]
    ]
 
    df = (
        prof.merge(glk, on="FIGHTER")
        .merge(divs, on="FIGHTER", how="left")
        .merge(sty, on="FIGHTER", how="left")
        .merge(res, on="FIGHTER", how="left")
    )
 
    # display positions: percentile rank on each axis, 0-100, computed across the
    # whole active universe so "high" and "low" are relative to the roster.
    df["comp_pct"] = df["RATING"].rank(pct=True).mul(100).round(1)
    df["prof_pct"] = df["public_profile"].rank(pct=True).mul(100).round(1)
 
    # under-booking percentile: among the scored, never-headlined fighters, how
    # far below their expected booking a fighter sits, expressed as a position in
    # that group (0-100). the residual is headlined - predicted, so a more
    # negative residual is more under-booked; ranking ascending then taking the
    # complement puts the most under-booked at the top of the scale. this is a
    # relative ordering within the roster, not a probability.
    under = df[(df["headlined"] == 0) & (df["residual"].notna())].copy()
    # ascending rank of residual: most negative (most under-booked) gets the
    # lowest rank, so 1 - pct gives the most under-booked the highest percentile.
    ranks = under["residual"].rank(pct=True)
    df["underbooked_pct"] = (1 - ranks).mul(100).round(0)
 
    return df
 
 
df = load_fighters()
 
# the weight-class menu is built from the primary (modal) division, so each
# fighter belongs to exactly one division rather than every one they have fought in.
DIVISIONS = sorted(df["primary_division"].dropna().unique())
 
 
# ----------------------------------------------------------------------------
# Sidebar filters and reading guide
# ----------------------------------------------------------------------------
st.sidebar.header("Filters")
 
wc = st.sidebar.selectbox("Weight class", ["All divisions"] + DIVISIONS)
 
# reliability filter: the single-source profiles are thinner readings, so allow
# hiding them, defaulting to showing everyone with the tag visible.
only_multi = st.sidebar.checkbox("Multi-source profiles only", value=False)
 
st.sidebar.caption(
    "The competitive axis is a Glicko-2 rating from UFC results. "
    "The public-profile axis is a three-signal attention composite. "
    f"Data frozen {FREEZE}."
)
 
with st.sidebar.expander("How to read this"):
    st.markdown(
        "**Competitive** and **Public profile** are percentiles from 0 to 100, "
        "measured against the active roster. A competitive score of 95 means the "
        "fighter's Glicko-2 rating is higher than 95 per cent of active fighters; "
        "the profile score works the same way on the attention composite.\n\n"
        "**Competitive axis**: a Glicko-2 rating built from UFC results, with a "
        "modifier for how convincingly each fight was won. It reflects the full "
        "career, not recent form alone.\n\n"
        "**Public profile axis**: an equally weighted composite of three attention "
        "signals, everyday Wikipedia pageviews, fight-week Wikipedia pageviews, and "
        "GDELT news-mention volume, each standardised before combining.\n\n"
        "**Under-booked**: measured relative to how fighters of similar merit and "
        "profile have historically been booked. Because that history favoured "
        "profile over merit, the flag is a conservative prompt to look, not a verdict."
    )
 
 
def apply_filters(frame):
    """Return the rows passing the current sidebar filters."""
    out = frame
    if wc != "All divisions":
        # a fighter passes if the chosen division is their primary (modal) one,
        # so each fighter appears in a single weight class rather than every
        # division they have ever fought in.
        out = out[out["primary_division"] == wc]
    if only_multi:
        out = out[out["profile_reliability"] == "multi_source"]
    return out
 
 
view = apply_filters(df)
 
 
# ----------------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------------
st.title("UFC Fighter Value Map")
st.write(
    f"Showing **{len(view)}** of {len(df)} active fighters "
    f"{'· ' + wc if wc != 'All divisions' else ''}"
)
 
 
# ----------------------------------------------------------------------------
# The two-axis scatter
#
# Each fighter is a point: competitive percentile on x, public-profile percentile
# on y. The diagonal is where profile matches competitive standing; distance from
# it is the divergence the framework is built to surface. Colour marks the rating
# reliability tier.
# ----------------------------------------------------------------------------
fig = px.scatter(
    view,
    x="comp_pct",
    y="prof_pct",
    color="TIER",
    category_orders={"TIER": ["Established", "Provisional", "Unreliable"]},
    hover_name="FIGHTER",
    hover_data={"comp_pct": ":.0f", "prof_pct": ":.0f", "TIER": True,
                "RATING": True},
    labels={"comp_pct": "Competitive (percentile)",
            "prof_pct": "Public profile (percentile)"},
    height=620,
)
# the agreement diagonal
fig.add_shape(type="line", x0=0, y0=0, x1=100, y1=100,
              line=dict(color="grey", dash="dash", width=1))
fig.update_traces(marker=dict(size=7, line=dict(width=0.5, color="white")))
fig.update_layout(legend_title_text="Rating reliability")
st.plotly_chart(fig, use_container_width=True)
 
 
# ----------------------------------------------------------------------------
# Two tabs: one fighter in detail, and the booking-model ranking
# ----------------------------------------------------------------------------
tab_detail, tab_booking = st.tabs(["Fighter detail", "Under-booked (booking model)"])
 
 
with tab_detail:
    name = st.selectbox("Choose a fighter", sorted(view["FIGHTER"]))
    f = df[df["FIGHTER"] == name].iloc[0]
 
    col1, col2 = st.columns(2)
    col1.metric("Competitive", f"{f['comp_pct']:.0f}",
                help="Percentile of the Glicko-2 rating across the active roster")
    col2.metric("Public profile", f"{f['prof_pct']:.0f}",
                help="Percentile of the attention composite across the active roster")
 
    # division line: primary division, noting the most recent weight where it
    # differs, so a fighter who has moved up or down is not silently relabelled.
    if pd.notna(f.get("last_division")) and f["primary_division"] != f["last_division"]:
        div_txt = f"{f['primary_division']} (last fought at {f['last_division']})"
    else:
        div_txt = f["primary_division"]
    st.write(f"**{div_txt}** · {int(f['N_FIGHTS'])} UFC fights · last out {f['LAST_FIGHT']}")
 
    # recent form: results of the last five bouts, oldest to newest, as context
    # for the career-long rating above.
    if isinstance(f.get("recent_form"), str) and f["recent_form"]:
        st.write(f"Recent form (last 5, oldest to newest): **{f['recent_form']}**")
 
    st.write(f"Rating **{int(f['RATING'])}** ({f['TIER']}) · "
             f"profile reliability: {f['profile_reliability'].replace('_', ' ')}")
    if pd.notna(f["primary_style"]):
        conf = f"{f['style_confidence'] * 100:.0f}%" if pd.notna(f["style_confidence"]) else ""
        st.write(f"Style: {f['primary_style']} {conf}")
 
    # the three profile signals, shown as raw pre-standardisation inputs and
    # tucked away, since the composite percentile above is the interpretable figure.
    with st.expander("Public-profile signals (raw inputs)"):
        st.caption("Raw signal values before standardisation and combination. "
                   "The profile percentile above is derived from these.")
        sig = pd.DataFrame({
            "signal": ["Everyday attention (Wikipedia baseline)",
                       "Fight-week attention (Wikipedia activation)",
                       "News coverage (GDELT)"],
            "raw value": [f["pv_baseline"], f["pv_activation"], f["gdelt_volume"]],
        })
        st.dataframe(sig, hide_index=True, use_container_width=True)
 
    # the booking readout is framed as an elevation signal for the post-PPV push
    # decision rather than a backward yes/no on past booking. it lays the model's
    # expectation next to what has actually happened, so the gap is visible: the
    # expectation is the share of similar-merit, similar-profile fighters that have
    # reached a headline slot; the actual is this fighter's own main-event history.
    # the model target is binary (ever headlined), so the expectation is a
    # likelihood of headlining, not a count.
    st.subheader("Booking")
    if pd.isna(f["residual"]):
        st.info("Not scored: the booking model covers Established and Provisional "
                "fighters with a multi-source profile only.")
    else:
        me = int(f["main_events"]) if pd.notna(f["main_events"]) else 0
        # expectation: predicted probability that a fighter with this merit and
        # profile has headlined, expressed as a percentage of comparable fighters.
        expect_pct = f["pred"] * 100 if pd.notna(f["pred"]) else None
        actual_txt = (f"has headlined ({me} main event{'s' if me != 1 else ''})"
                      if f["headlined"] == 1 else "has not headlined (0 main events)")
 
        under = (f["headlined"] == 0 and pd.notna(f.get("underbooked_pct"))
                 and f["underbooked_pct"] >= 70)
        over = f["headlined"] == 1 and f["residual"] >= 0.3
 
        if under:
            st.warning(f"**Candidate for elevation.** Merit and profile sit ahead of "
                       f"booking: among the most under-booked in the division.")
        elif over:
            st.info(f"**Booked ahead of merit.** Has headlined despite merit and "
                    f"profile sitting below the level that usually accompanies a "
                    f"headline slot.")
        else:
            st.success("**Booked broadly in line with merit and profile.**")
 
        # the expected / actual / context block that shows the reasoning, not just
        # the verdict.
        exp_line = (f"about {expect_pct:.0f} per cent of comparable fighters"
                    if expect_pct is not None else "comparable fighters")
        st.markdown(
            f"- **Model expectation**: {exp_line} of similar merit and profile "
            f"have reached a headline slot.\n"
            f"- **This fighter**: {actual_txt}, across {int(f['N_FIGHTS'])} UFC fights.\n"
            f"- **Reading**: a prompt to look, not a verdict; the expectation is drawn "
            f"from how similar fighters have historically been booked."
        )
 
 
with tab_booking:
    st.write(
        "Candidates for elevation: fighters whose merit (competitive rating and "
        "public profile) sits ahead of the booking they have received, ordered by "
        "the size of that gap. The gap is measured relative to how fighters of "
        "similar merit and profile have historically been booked, so it is a prompt "
        "to look, not a verdict. Fight count is shown as context, since a high-merit "
        "newcomer and a passed-over veteran are different cases."
    )
 
    # under-booked = scored, never headlined, most under-booked first. apply the
    # same weight-class filter as the rest of the page.
    ranked = apply_filters(
        df[(df["headlined"] == 0) & (df["residual"].notna())]
    ).sort_values("residual").reset_index(drop=True)
 
    # rank is the position in the sorted shortlist: 1 is the most under-booked in
    # the current filter. clearer than a bare percentile in a table column.
    ranked.insert(0, "rank", ranked.index + 1)
 
    show = ranked[["rank", "FIGHTER", "primary_division", "RATING", "comp_pct",
                   "prof_pct", "N_FIGHTS", "TIER"]].copy()
    show["RATING"] = show["RATING"].round(0)
    show = show.rename(columns={
        "primary_division": "division",
        "comp_pct": "comp %ile",
        "prof_pct": "profile %ile",
        "N_FIGHTS": "fights",
        "TIER": "reliability",
    })
    st.dataframe(show.head(25), hide_index=True, use_container_width=True)
    st.caption(f"{len(ranked)} under-booked fighters"
               f"{' in ' + wc if wc != 'All divisions' else ' across the roster'}. "
               f"Ranked most under-booked first.")
 
