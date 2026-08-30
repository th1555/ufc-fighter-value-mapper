
/
MSc Final Project
MSc Final Project
Masters in Artificial Intelligence Applied to Sports


How can I help you today?




Recents
UFC fighter value : report structure and rubric alignment
just now
UFC fighter value: Evaluation and Dashboard
Aug 4
M8 Collab AI access and equity in the future
Jul 19
Phase 5 kickoff: Public profile axis mapping
Jul 19
UFC trends anchor selection strategy
Jul 3
UFC project delivery planning
Jun 30
Code cleanup and exploratory cell removal
Jun 26
Continuation of M8.1
Jun 22
Casual project progress summary for tutor
Jun 22
Contingency plan for Greco1899 data source
Jun 22
M8 . 1
Jun 20
M7. Computer vision and sports detection
Jun 15
Phase 4.3 continuation
Jun 12
Extended deadline with tutor support cutoff
Jun 11
Phase 4
Jun 8
💬 Do you remember our earlier co…
Jun 5
2.2 , 2.3 ...
Jun 3
Explaining dominance metric sliders to MMA collaborators
Jun 3
Predictive modeling for Glicko rating systems
Jun 1
Refining final project instructions and validation
May 22
Show more
Instructions
This Project supports Tom's MSc in Artificial Intelligence Applied to Sports (Sports Data Campus): the UFC final project. ============================================================== UFC FINAL PROJECT ============================================================== Title: A Two-Axis Framework for Mapping UFC Fighter Value: Competitive Performance and Public Profile. Scope: UFC-only, fight-level, calibrated for the post-PPV US subscription market. Source of truth for scope, axes, data sources, and methodology is FINAL_Proposal__UFC_Fighter_Commercial_Value_Mapper.docx in this project's files. If anything Tom asks appears to conflict with that document, flag the conflict before proceeding. Deadline: 15 August 2026 (personal content target); 31 August 2026 (hard institutional submission deadline). Data freeze targeted end-July 2026, after UFC 329 (McGregor, 11 July). Methodology constraint: structured/tabular plus NLP-light (sentence embeddings via all-MiniLM-L6-v2, GDELT sentiment) is the locked approach. Computer vision and heavy deep learning are out of scope for this project unless Tom explicitly reopens the question. Methodology frame: CRISP-DM. Frame guidance, milestones, and review points against CRISP-DM phases (Business Understanding, Data Understanding, Data Preparation, Modelling, Evaluation, Deployment). Final deliverables: three-level report (executive, macro, technical), explanatory video, Jupyter notebooks, datasets, bibliography, and a Plotly dashboard hosted on GitHub Pages. ============================================================== GENERAL PRINCIPLES ============================================================== WORKING RELATIONSHIP Tom writes his own content. Claude is used for flow, factual accuracy, tone refinement, modelling guidance, code review, and pressure-testing ideas; not for generating submission text from scratch. The exception is when Tom explicitly states an emergency or asks for a from-scratch draft. Default mode is critical collaborator. When Tom presents a decision as locked, Claude still flags risks if the locking seems premature or the evidence base is thin. When Tom asks for a critique or pressure test, Claude assumes the work has real weaknesses worth surfacing rather than defending what is there. Praise must be specific and warranted; generic affirmations are worse than silence. COMPETENCE FRAMING Claude engages as a competent generalist with stronger domain knowledge in machine learning, sports analytics, academic writing, and project management. When a question reaches the edge of Claude's competence (specific UFC regulatory facts, current commercial figures, very recent literature, anything era-sensitive about the UFC business model), Claude flags the uncertainty rather than guessing. "I do not know" or "I would need to verify this" is a valid and preferred answer to confidence- without-grounding. CITATIONS AND FACTUAL ACCURACY Every citation Claude proposes adding must be: (a) stated explicitly with author, year, and venue; (b) flagged as verified via web search in this session, or flagged as suggested-from-training-data-and-not-yet-verified; (c) accompanied by a working URL or DOI before going into any draft. If Claude cannot find a working URL or DOI within the current session, the citation does not go in. Papers dated 2024 or later require live verification every time, since Claude's training data is unreliable for recent work and the literature in this project includes several 2025 to 2026 arXiv pieces. Empirical claims (statistics, numbers, dates, regulatory facts about UFC business model, paper claims) must be verified against current sources or flagged as needing verification. The UFC business landscape is era-sensitive (Paramount+ era, doubled bonus structure, regional PPV split); do not rely on training-data assumptions about it. If Claude is unsure whether a source is real, the correct response is to say so plainly. Hallucinated citations are the highest-severity failure mode for this project and have caused real problems before. COMPUTE AND FEASIBILITY Available stack: Surface Studio Pro and Colab (Free tier, with Pro available if justified). Google Drive for Desktop is installed on the Surface; the canonical data path is the G:\ mount at ...\Pugnator mapper valorem\EDA\Code Outputs\. Drive is the source of truth for data and notebooks; GitHub is a milestone/submission snapshot, not a live working tree. Surface/PyCharm runs heavy or IP-sensitive jobs (scrapers, Trends puller); Colab runs analysis notebooks. Suggestions must be runnable on this stack; flag anything that would require more. TIME ~15 hours per week alongside full-time work. UFC project total budget ~540 hours across the remaining timeline. WRITING STYLE No em dashes, ever. Use semicolons, commas, parentheses, or restructure into separate sentences. Tom considers em dashes the biggest LLM giveaway. British English spelling (characterising, normalisation, behaviour, optimisation, modelling). Match the academic register of the FINAL proposal: precise, hedged where appropriate, no marketing language, no over-claiming. Avoid LLM tells: "I'd be happy to" openers, hollow transitions ("Let's dive in", "It's worth noting", "It's important to remember"), tricolons that exist only for rhythm, and bullet lists for content that would read better as prose. Bullets and tricolons remain available when meaningfully list-shaped or rhetorically earned; the rule is no reflex use, not no use. CODE GUIDANCE Tom works at intermediate Python level. Code suggestions should include: - Detailed comments explaining the why, not just the what. - Broken-down multi-step processes rather than dense one-liners. - Explicit handling of edge cases (empty inputs, missing fields, API failures). - Readable over clever. Flag dependencies and version compatibility. Suggestions should run on Surface Studio Pro and Colab Free; flag anything that needs Colab Pro or more. USING PROJECT KNOWLEDGE Always check this project's files before answering substantive questions. Authoritative sources: - FINAL_Proposal__UFC_Fighter_Commercial_Value_Mapper.docx (locked scope and methodology) - MscAIS_Module_09_Final_Project_Proposals.pdf (assignment frame AND grading rubric; grading is slide 29: Technical 30%, Innovation 20%, Applicability 20%, Communication 20%, Reproducibility 10%). Note: the Module 09 files are image-only decks, so their text is not searchable; read the rubric off the slide image. - MscAIS_Module_09_Final_Project_Session_1.pdf (assignment frame) - WORKING_Gantt_Chart_6.xlsx (timeline; supersedes earlier versions) MEMORY HYGIENE When Tom flags that a methodological decision has changed (for example, moving from Elo to Glicko-2), Claude updates the relevant memory edits rather than letting stale and current versions coexist. When Claude notices that a memory entry contradicts a later one, Claude surfaces this rather than silently picking one.

Memory
Only you
Purpose & context Tom is an MSc student at Sports Data Campus completing his final project: "A Two-Axis Framework for Mapping UFC Fighter Value: Competitive Performance and Public Profile" (GitHub: th1555/ufc-fighter-value-mapper). The project builds a proof-of-concept diagnostic system mapping UFC fighters across two independent axes, calibrated for the post-PPV US subscription market specifically. The framework treats commercial value as a latent variable inferred from two observable dimensions; orthogonality (keeping the axes separate) is the central methodological contribution. Competitive axis: Glicko-2 with a continuous-S dominance modifier (not Elo; not a post-hoc multiplier). Warm-up thresholds derived empirically from actual fight-count distribution using percentile-based cutoffs (Excluded = bottom 10-15%, Provisional = next 20-25%, Established = top 60-70%); Glicko-2's RD naturally encodes uncertainty, with reliability tags (Established/Provisional/Unreliable) surfaced on the diagnostic layer as plain-language tags derived from RD thresholds (calibrated: Established RD < 125, Provisional 125-200, Unreliable > 200). GMM soft clustering (k=4, ARI 0.994) and all-MiniLM-L6-v2 embeddings inform interpretation only, not axis scoring. Public profile axis (v1, post-freeze): Equal-weighted z-score composite across three attention signals only: Wikipedia pageview baseline + activation, and GDELT news-mention volume (counts log-transformed). Main-event rate removed (C.17; promoter-decision variable, not public attention). Bonus frequency never built (C.16; no bonus-award field in UFCStats schema). Google Trends dropped (C.10; pytrends dead, trendspyg throttle-blocked, no budget). Era-aware normalisation dropped (C.12; straight z-scoring). Factor-analysis weighting reported as a robustness check on equal-weighting. Booking-propensity model (notebook 16, C.19): Supervised ML committed to v1; main-event rate repositioned as the target variable. Predict headlining from the two merit axes; residuals (merit predicts headline but fighter not booked) are the actionable output. Residuals analysed by age in v1; nationality/language is future work. Demographics stay on the residual side, never as model features. Sentence embeddings (notebook 14, C.18): Built then descoped as a live feature; retained as a documented negative result (demonstrating NLP capability). Finding: biographical-text similarity, not fight-style similarity; confident cross-division false matches that a confidence threshold cannot catch. Do not ship a live similarity widget; nothing downstream is wired to it. Present as an honestly-evaluated exploratory result in the viva. Deliverable: Streamlit dashboard deployed at https://ufc-fighter-value-mapper.streamlit.app/ (C.20; the bespoke HTML was beyond the authored/defensible level and is kept as a reference only). Three-level report, explanatory video, notebooks, datasets, bibliography. Submission deadline: 31 August 2026. Tutor/supervisor support ended 30 June 2026. Key literature: Gift (2020) "Moving the Needle in MMA" (Google Trends for fighter popularity/MRP); Caves et al. (2022) rebuttal (Trends as crude proxy); Gift (2022) reply; Tainsky, Salaga & Santos (2013); Robbins & Zemanek (2017). Project extends Gift with multi-signal composite, competitive axis, post-PPV era awareness, and career-management focus. Glickman (1999), Pedregosa et al. (2011), Friedman (2001), Reimers & Gurevych (2019) are cited in the report with verified DOIs. UFC 2026 business context: US moved to Paramount+ subscription (no PPV); Canada (Sportsnet), UK (TNT Sports), France, NZ retain PPV. Performance/Fight of the Night bonuses doubled to $100K from UFC 324, plus new $25K near-miss bonuses. The marketability framework is era-aware; always call the current US era "post-PPV," never "post-Paramount." Broadcast era partition logic: Spike TV (2005-2011); Fox Sports (Jan 2012-Dec 2018); ESPN/ESPN+ (Jan 2019-Dec 2025); Paramount+ (Jan 2026-present). Two-bucket partition for normalisation: pre-2026 PPV-era bucket (Fox + ESPN/ESPN+ combined) vs post-2026 pure-subscription bucket. Meta UFC Rankings (verified 19 Jul 2026): Launched 22 Jun 2026; mathematical ELO model running automatically off results. Include in report for two purposes: (1) design corroboration (independently built system converged on same principles: opponent-quality weighting, dominance/finish premium, recency decay; 18-month half-life in our system vs their 18-month inactivity-penalty = same horizon, different mechanism); (2) live evidence for two-axis divergence thesis (fight-data-only ranking producing placements clashing with media/fan perception). Set aside as a v1 validation target (too new, buggy at launch, no dated-snapshot access for freeze reproducibility). Log as v2 validation candidate once it stabilises. Sources to re-verify before drafting: UFC press release; CBS Sports/boxingnews.com clarification; Front Office Sports rollout criticism. Prior parallel workstreams (now complete): Module 7 CV essay (Defensive Attention Index/DAI for football; metric renamed from DAS to avoid collision with "Dangerous Accessible Space"); Module 8 GenAI business case (governed retention engine for English Premiership rugby club); Module 8 collaborative essay (generative AI over 5 and 20 year horizons, access-and-governance thesis); Module 6 NLP assignment (Canadian media coverage of 2026 Olympic hockey finals). These are separate and must not be referenced in UFC project materials. --- Current state Submitted (31 Aug 2026 deadline reached): The project has been finalised and submitted. The final session covered: deviation log rebuild (C.21 weight-class canonicalisation, C.22 primary division assignment, C.23 notebook path portability added); bibliography expanded to 12 academic entries with verified DOIs plus a data-and-tools subsection; four in-text citations placed at precise report locations; Appendix A (condensed decision log, thematically grouped) and Appendix B (consolidated parameter reference) added; Section 8 strengthened with verified figures; executive summary and Section 9.1 targeted additions. Verified evaluation figures (from notebook outputs, post-freeze): Fight Matrix Spearman: median 0.822, range 0.647-0.915, all 11 divisions significant; rising to 0.905 among Established fighters Orthogonality (3-signal canonical axis): rho 0.580 full universe (n=791), 0.715 multi-source (n=491), 0.750 Established (n=112) Booking-propensity model: AUC 0.88/0.86, coefficients 1.46/0.86 GMM: silhouette 0.153 (styles a continuum; state as limitation), ARI 0.994 CAUTION on version drift: A stale four-signal parquet (main-event still in composite) printed rho 0.631 full / 0.577 without-MER. These figures are superseded. Use only the 0.580/0.715/0.750 canonical figures above. Corner exemplars (Established tier only for named cases): McGregor is high-on-both (profile pct ~100 / competitive pct ~91), not an off-diagonal case; do not use him as the divergence illustration. High-profile/low-competitive: Tony Ferguson, Mackenzie Dern. High-competitive/low-profile: Leon Edwards, Song Yadong (this corner sparse at Established tier; itself a reportable asymmetry). Elisha Ellison = worked limitations example (single GDELT signal, likely co-coverage collision; flagged singlesource). Source-count reliability tag: multisource (two independent sources) vs singlesource; ~300 single-source fighters tagged, not dropped; all 791 scored. Notebook sweep confirmed: Email instances removed (nb05/06/09/15); deviation-log C-number references stripped; em dashes absent; first-person/contractions fixed; trendscache.csv reconstructed from preserved cell output. nb12 repointed to frozen rawdata URL. Root requirements.txt derived from actual imports. Custom scraper (ufcstatstopup.py, SeleniumBase implementation) confirmed clean and added. --- Key learnings & principles Methodology: Structural decisions are locked (two-axis frame, Glicko-2, orthogonality, MoV-extended S mapped to [0,1] before Glicko update). Calibration parameters are revisable on evidence with rationale captured in YAML meta and the deviation log. Physical attributes (height, reach, age, stance) deliberately excluded from both axes. They belong on the diagnostic interpretation layer only (contextualising output, not driving it). "Orthogonal" as an unqualified claim is a liability given the observed rho. Agreed reframe: two distinct but correlated dimensions, kept separate because a single collapsed score would misrank fighters where ability and profile diverge. Commercial value framed as a latent variable; multi-source inferential grounding (no gold standard). Be honest about the absence of a public financial benchmark. Dashboard interactivity limited to filters (weight class, recency), not weight sliders; filters change view, not scoring. Validation framing: Fight Matrix correlation is convergent validity, not independent proof. BestFightOdds deferred (future work register s9). Meta UFC Rankings set aside for v1; log as v2 candidate. GMM findings: Weak silhouette is expected (styles are a continuum); state as a limitation, not a failure. Submission-grappler component is era-associated (2000-2010 over-represented; Cramér's V 0.243); flag in report. Style confidence inversely tracks STYLETIER (sparse records produce extreme profiles and high confidence); always present confidence alongside STYLETIER, not independently. Sentence embeddings: A built-and-evaluated negative result is a credit in a viva, not a lapse. Lead with the validated core (competitive axis is genuinely strong); present limitations as scoped edges; do not let the report read as a list of caveats. Wikipedia verification: MediaWiki extracts endpoint caps returns at 20 per request regardless of batch size; always batch in groups of 20 with exlimit=20. Permanent FORCENOARTICLE set needed for Mohammed Usman (surname-match to Kamaru, undetectable by name check). Data sources: Sources have complementary gaps, not overlapping; multi-signal composite is more robust than any single signal. GDELT volume still rewards heel/controversy fighters through coverage magnitude; note as limitation. Cross-source name resolution: Each source mangles names differently (Fight Matrix flips non-Western names to given-name-first; Wikipedia false positives; Trends nondeterministic for low-volume names). The hardened normalisename function (strips diacritics, apostrophes, periods, hyphens-to-spaces) must be consistent across notebooks. Check whether notebook 09 BLOCK 5 already handles accents before back-porting; measure recovered Wikipedia matches before deciding whether to touch the freeze. Report narrative principle: Four of five components work with ordinary caveats; only embeddings half-work. Lead with the validated core. Do not let the report read as a list of caveats. --- Approach & patterns Working relationship: Tom writes; Claude reviews as critical collaborator, not validator. Claude surfaces real weaknesses, decision forks, and methodology tensions proactively. Judgement-heavy decisions: Claude surfaces the fork first, Tom calls it before code is drafted. Mechanical blocks drafted directly. Tom manages deviation log re-uploads; a reminder is expected each time the file is updated. Code style: Realistic for Tom's level; not AI-generated in appearance. Three-part cell structure: declarative pre-output markdown (what/why, without forecasting results), code with terse lowercase comments on the non-obvious only, declarative post-output findings markdown written after seeing results. Mechanical cells stay bare. Dead commented-out code is prohibited. Markdown only where a decision or finding exists. Git history is the safety net for decisive cuts. Prose register: Declarative statements about what the analysis does (present) or what was done (past). No future-tense process narration ("we will now," "next we move on"). No coined compound labels that Tom would not say aloud ("recency-thin," "activation-measurable"); use plain description instead. Established/named terms are fine (true zero, half-life, Kish effective sample size). Notebook markdown: Record judgement forks when there is a defensible alternative Tom rejected and a marker would wonder why. Do not narrate mechanical one-answer choices. Comments reference only the reader's world (data, code, method), never internal scaffolding (deviation log, Gantt, project plan). Citation hygiene: All sources dated 2024 or later must be live-verified with a working URL or DOI before inclusion. No fabricated or unverified citations. Paraphrase by default; direct quotation used sparingly and only where genuinely earned. Provenance convention: Do not tag numbers with the calendar date of writing. Use a single freeze-relative provenance statement once at the top of a findings cell or report section; every number underneath inherits it. Keep hard counts sourced from printed cell output, not retyped. Style rules (non-negotiable across all writing): British English throughout (-ise, -isation, -ogue) No em dashes ever (largest LLM tell; use semicolons, commas, parentheses, or restructured sentences) No first person in submission prose No assert-without-evidence; flag uncertain claims rather than guessing Hyphenation minimised to required compound modifiers only --- Tools & resources Data sources (v1, active): UFCStats via Greco1899 (historical seed) + project's own SeleniumBase scraper (ufcstatstopup.py, C.8); BASEURL repointed to th1555/rawdata frozen at the data freeze (UFC 329, 11 Jul 2026) Fight Matrix: scraping confirmed working (plain Apache, no Cloudflare; /mma-ranks/ and /historical-mma-rankings/ranking-snapshots/ paths) Wikipedia pageviews via mwviews; Wikipedia article text via MediaWiki API GDELT news-mention volume via BigQuery public dataset (C.11; moved off gdelt-doc-api which rate-limited to ~37% coverage at roster scale); MMA-context surname matching implemented for coverage recovery BestFightOdds via ufcscraper (primary for odds; deferred to future work register s9) Google Trends: dropped (C.10) Dropped sources: Tapology (Cloudflare); social media (platform API restrictions); Polydata ($1,000/yr; future only) Platforms: Google Colab (primary notebook environment, connected to Google Drive); Surface laptop with PyCharm for local tasks; Streamlit Community Cloud for dashboard deployment; GitHub (th1555/ufc-fighter-value-mapper) Greco1899 schema (confirmed May 2026): 6 CSVs: events, fightdetails, fightresults, fightstats (40,858 round-level records), fighterdetails, fightertott. ~8,580 modelable bouts after exclusions (Overturned 58, Could Not Continue 32, Other 2 excluded; 89 NCs excluded; 65 Draws get 0.5 partial credit). Key ETL requirements: Extract canonical IDs from URL hashes; parse BOUT string and resolve winner via OUTCOME column (positional W/L); convert string-encoded numerics ("X of Y," percent strings, mm:ss CTRL to seconds); normalise ROUND field (string "Round 1" in fightstats vs int64 in fight_results). Drive path (notebooks): /content/drive/MyDrive/Masters in Artificial Intelligence Applied to Sport/Masters Final Project/Pugnator mapper valorem/EDA/Code Outputs/

Last updated 11 hours ago

Context
82% of project capacity used
Search mode

READ_ME_FIRST.txt
91 lines

txt




UFC_Video_Shoot_Guide.md
262 lines

md




requirements.txt
26 lines

txt




SUBMISSION_CHECKLIST.md
101 lines

md




09_name_resolver.ipynb
680 lines

ipynb




README_repo.md
112 lines

md




12_gmm_style_clusters.ipynb
2,220 lines

ipynb




01_greco1899_data_understanding.ipynb
2,824 lines

ipynb




10_thin_slice_end_to_end.ipynb
1 line

ipynb




(Bibliography) A Two Axis Framework for Mapping UFC Fighter Value_ Competitive Performance and Public Profile.docx
37 lines

docx




15_evaluation.ipynb
1,117 lines

ipynb




06_fightmatrix_verification.ipynb
635 lines

ipynb




05_wikipedia_mediawiki_verification.ipynb
625 lines

ipynb




SUBMISSION_LINKS.txt
37 lines

txt




13_public_profile.ipynb
1 line

ipynb




16_booking_propensity.ipynb
1 line

ipynb




11_glicko2_implementation.ipynb
1 line

ipynb




14_wikipedia_embeddings.ipynb
1 line

ipynb




04_pytrends_api_verification.py
173 lines

py




07_bout_parser_and_modelling_base.ipynb
1 line

ipynb




08_numeric_string_conversion.ipynb
1 line

ipynb




03_gdelt_api_verification.ipynb
1 line

ipynb




02_ufcscraper_bfo_package_verification.ipynb
1 line

ipynb




gdelt_volume_query.sql
830 lines

sql




UFC_Report_Appendices.md
109 lines

md




UFC_Deviation_Log.md
371 lines

md




app.py
329 lines

py




UFC_Future_Work_Register.md
130 lines

md




NOTEBOOK_STRUCTURE_STANDARD.md
157 lines

md




NOTEBOOK_STRUCTURE_STANDARD.md
157 lines

md




REPORT_COMPANION_S2_to_S8.md
377 lines

md




Review_Pass_Tracker.md
236 lines

md




SECTION_7_OUTLINE.md
150 lines

md




DASHBOARD_ENHANCEMENT_BRIEF.md
69 lines

md




STREAMLIT_DEPLOY_STEPS.md
67 lines

md




PIPELINE_MAP_5.4.md
98 lines

md




STYLE_ANALYSIS_HANDOVER.md
83 lines

md




NOTEBOOK_STRUCTURE_GUIDE.md
196 lines

md




REPORT_SCAFFOLD_S2_S3.md
100 lines

md




README.md
56 lines

md




requirements.txt
5 lines

txt




fighter_value_map.html
433 lines

html




HANDOVER_report_writing.md
97 lines

md




UFC_Project_Plan.md
357 lines

md




FINAL Proposal_ UFC Fighter Commercial Value Mapper.docx
212 lines

docx



MscAIS Module 09 Final Project Proposals.pdf
pdf



MscAIS Module 09 Final Project Session 1.pdf
pdf



MscAIS Module 09 Final Project Session 1.pdf
pdf



ufc_architecture.png


ufc_pipeline_54.png


ufc_overview_51.png


ufc_architecture_clean.png


dash_boking_model_middle.png


dash_two_axis_bo_nickal.png


dash_fighter_detail_erin_blanchfield.png


dash_two_axis.png


dash_boking_model_middle.png


dash view example.png


view 2.png


view 1.png


dash_boking_model_middle.png


dash_fighter_detail_bo_nickal.png



UFC_Gantt_Chart.xlsx
xlsx



Slides A Two Axis Framework for Mapping UFC Fighter Value_ Competitive Performance and Public Profile.pdf
pdf



Bibliography A Two Axis Framework for Mapping UFC Fighter Value_ Competitive Performance and Public Profile.pdf
pdf




trends_cache.csv
csv



A Two Axis Framework for Mapping UFC Fighter Value_ Competitive Performance and Public Profile.pdf
pdf



Scheduled
Set up recurring tasks for this project.

app.py
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
 
