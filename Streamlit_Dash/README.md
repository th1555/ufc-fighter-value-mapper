# UFC Fighter Value Map: dashboard
 
An interactive dashboard for the two axis fighter value framework. It shows the
competitive and public profile axes as a scatter, a per fighter detail view, and
the booking-propensity model's under-booked ranking, filterable by weight class.
 
## What is in this folder
 
    app.py                     the Streamlit application
    requirements.txt           pinned dependencies
    README.md                  this file
    data/                      the parquet inputs (see below)
 
## Data files
 
The app reads five parquet files from a `data/` folder next to `app.py`. Copy
them from the pipeline's Code Outputs folder:
 
    data/public_profile_axis.parquet        public profile axis (three-signal)
    data/glicko_current_continuous.parquet  competitive axis (Glicko rating, tier)
    data/style_clusters.parquet             GMM style archetype per fighter
    data/booking_residuals.parquet          booking propensity model output
    data/fighter_divisions.parquet          each fighter's weight class(es)
 
If any are missing, the app says which ones rather than crashing.
 
## Run it locally
 
1. Install Python 3.11 or newer.
2. In this folder, create and activate a fresh virtual environment.
3. Install the dependencies:
       pip install -r requirements.txt
 
4. Put the five parquet files into a `data/` subfolder.
5. Start the app:
       streamlit run app.py
 
   It opens in your browser at http://localhost:8501
## Deploy to Streamlit Community Cloud
 
1. Push this folder (including `data/` and `requirements.txt`) to a GitHub repo.
2. At share.streamlit.io, sign in with GitHub and choose "New app".
3. Point it at the repo and `app.py`. It installs from `requirements.txt` and
   builds the app. The public URL is the submission link.
## Note on reproducibility
 
`fighter_divisions.parquet` was captured from the earlier dashboard build rather
than regenerated from the frozen fight results. Regenerating it directly from
`ufc_fight_results.csv` (weight class per bout, aggregated per resolved fighter)
is a small outstanding step; the division data itself is correct and does not
change with the axis rebuild.
 
