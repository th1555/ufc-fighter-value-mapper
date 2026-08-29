# A Two Axis Framework for Mapping UFC Fighter Value

Competitive performance and public profile, measured on separate axes, with a booking propensity model that reads the gap between them.

This repository holds the code, data, and dashboard for an educational project. The framework places each UFC fighter on two axes: a competitive axis (a Glicko-2 rating with a continuous dominance modifier) and a public profile axis (an attention composite from Wikipedia pageviews and GDELT news coverage). The relationship between them exposes booking patterns and identifies under-booked prospects.

## Live dashboard

The interactive two axis map, per fighter detail, and the under booked ranking are deployed here:

https://ufc-fighter-value-mapper.streamlit.app/

## Repository structure

```
notebooks/            the analysis, numbered 01 to 16 in run order
  data/               intermediate outputs the analysis notebooks read and write
raw_data/             the frozen UFCStats source data (six CSVs)
sql/                  the GDELT BigQuery query used for the news-volume signal
Streamlit_Dash/       the dashboard application
  app.py              the Streamlit app
  data/               the five parquets the dashboard reads
  requirements.txt    dashboard dependencies
  README.md           dashboard specific notes
.devcontainer/        development container configuration
requirements.txt      analysis dependencies
README.md             this file
```

## The notebooks

The notebooks run in numbered order. The early notebooks verify and acquire each data source; the later notebooks build the axes, the models, and the evaluation.

- 01 to 06: source verification and acquisition (UFCStats, GDELT, Wikipedia, Fight Matrix). These reach live external services and are provided as a record of how the data was obtained.
- 07 to 09: data preparation. Parsing the raw records, converting them to numeric form, and resolving fighter identity across sources.
- 10: a thin end-to-end slice used to validate the pipeline shape before the full build.
- 11: the competitive axis (Glicko-2 with the dominance modifier).
- 12: the style layer (Gaussian mixture clustering).
- 13: the public profile axis (the pageview and news volume composite).
- 14: the Wikipedia embedding component, built and evaluated, and reported as a negative result.
- 15: evaluation (convergent validity against Fight Matrix, the two axis relationship).
- 16: the booking propensity model and its residuals.

## Running the analysis

The notebooks are written to run in Google Colab or in a local Jupyter environment without modification. The data path resolves automatically: if a Google Drive mount is present it is used, otherwise the path is local.

To run locally:

1. Clone the repository.
2. Install the dependencies: `pip install -r requirements.txt`
3. Open the notebooks in `notebooks/` and run them in numbered order.

The analysis notebooks (07 to 16) read the intermediate outputs in `notebooks/data/`, so they reproduce the axes, models, and results directly from the frozen data without re-running the acquisitions.

## Running the dashboard

```
cd Streamlit_Dash
pip install -r requirements.txt
streamlit run app.py
```

The app reads the parquets in `Streamlit_Dash/data/` and regenerates its views from them, so it reflects the state of the pipeline rather than a fixed copy.

## Reproducing the results

There are two levels of reproduction. Most readers will want the first.

### Re-running the analysis from the frozen data

The analysis notebooks (07 to 16) read the intermediate outputs already provided in `notebooks/data/`, so they reproduce the axes, the models, and the reported figures directly, without re-pulling from live services. This is the fastest path to results and requires only the dependencies, not external service access.

1. Clone the repository.
2. Install the dependencies: `pip install -r requirements.txt`
3. From inside the `notebooks/` directory, run the notebooks in numbered order. Each reads its inputs from `notebooks/data/` and writes its outputs back to the same folder.

Run the notebooks from within `notebooks/` so the relative data path resolves. The raw source data is read over the network from `raw_data/` in this repository, so no local raw files are required.

### Re-pulling from source (a new freeze)

The acquisition notebooks (01 to 06) pull from live services (GDELT via BigQuery, the Wikimedia Pageviews API, Fight Matrix, and UFCStats through the project scraper). Re-running these produces a new data freeze. Notebooks 07 onwards will then operate on the new snapshot.

### Refreshing the dashboard after a re-run

The dashboard reads its own copy of the outputs from `Streamlit_Dash/data/`, which is separate from `notebooks/data/`. Re-running the notebooks does not update the dashboard automatically. To refresh the deployed dashboard after a full re-run, copy these five files from the notebook outputs folder into `Streamlit_Dash/data/`:

- `public_profile_axis.parquet`
- `glicko_current_continuous.parquet`
- `style_clusters.parquet`
- `booking_residuals.parquet`
- `fighter_divisions.parquet`

Copy those five from the output location into `Streamlit_Dash/data/`, then restart the app. Until they are copied, the dashboard continues to show the previous freeze.

## Reproducibility and the data freeze

The analysis is built on data frozen at 11 July 2026, the date of the last fight in the dataset (UFC 329). Every downstream window (the active fighter cut, the pageview history, the news coverage window) is defined relative to that date. Notebooks 07 onwards operate deterministically on that snapshot; notebooks 01 to 06 are provided for reference and as a log of the data acquisition, not for re-execution in a production setting.

Several signals are drawn from live sources: GDELT via its public BigQuery dataset, Wikipedia pageviews via the Wikimedia API, and Fight Matrix and UFCStats via their public pages. These cannot be frozen perfectly and will change with time. The snapshot is nonetheless reproducible in the sense that:

- The notebooks that consume the frozen data (07 to 16) always produce the same outputs from it.
- The source acquisition notebooks (01 to 06) are included so the method is visible and reproducible by anyone who chooses to re-pull.

## Data sources

- UFCStats (http://ufcstats.com/), fight and fighter statistics, seeded from the Greco1899 scrape_ufc_stats snapshot (https://github.com/Greco1899/scrape_ufc_stats) and topped up by an independent scraper written for this project (scripts/ufc_stats_topup.py), which keeps the data current as the Greco1899 mirror periodically stalls.
- Custom scraper (ufc_stats_topup.py). An independent scraper written for this project against the public UFCStats pages, used to keep the fight data current after the upstream Greco1899 mirror snapshot aged.
- GDELT Project (https://www.gdeltproject.org/), news-coverage volume via the Global Knowledge Graph.
- Wikimedia Foundation, pageview data via the Wikimedia Pageviews API, accessed with python-mwviews (https://github.com/mediawiki-utilities/python-mwviews).
- Fight Matrix (https://www.fightmatrix.com/), used as an independent validation benchmark.

## Licence and attribution

The fight data originates from UFCStats and is credited above. The Greco1899 snapshot provides the historical seed; the project's own scraper is an independent implementation. Fighter statistics and identities are factual information and not subject to copyright. Analysis, code, visualisation, and presentation are the author's own work.
