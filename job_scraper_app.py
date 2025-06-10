import streamlit as st
import pandas as pd
import time

# Simulated job scraper (replace with real scraper later)
def scrape_jobs():
    data = [
        {"Job Title": "Financial Analyst", "Company": "Kforce", "Location": "Remote", "Link": "https://www.kforce.com/jobs"},
        {"Job Title": "Financial Analyst", "Company": "Robert Half", "Location": "Orlando, FL", "Link": "https://www.roberthalf.com/jobs"},
        {"Job Title": "Sr. Financial Analyst", "Company": "Insight Global", "Location": "Remote", "Link": "https://www.insightglobal.com/jobs"},
    ]
    return pd.DataFrame(data)

# Streamlit UI
st.set_page_config(page_title="Job Scraper App", layout="wide")
st.title("📊 Financial Analyst Job Scraper Dashboard")

with st.sidebar:
    st.header("Filters")
    test_mode = st.checkbox("Test Mode", value=True)
    keyword = st.text_input("Keywords", "financial analyst")
    run_search = st.button("Run Job Search")

if run_search:
    with st.spinner("Scraping job boards..."):
        time.sleep(2)
        jobs = scrape_jobs()
        st.success(f"Found {len(jobs)} jobs!")
        st.dataframe(jobs)
        for i, row in jobs.iterrows():
            st.markdown(f"- [{row['Job Title']} at {row['Company']}]({row['Link']}) — {row['Location']}")
            if not test_mode:
                st.info("✅ Application submitted!")
            else:
                st.info("🔎 Test mode only — no apply.")
else:
    st.info("Click 'Run Job Search' to begin.")
