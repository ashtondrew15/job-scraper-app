import streamlit as st
import pandas as pd
import time
from datetime import datetime

# Set up the Streamlit page
st.set_page_config(page_title="Finance Job Scraper", layout="wide")

# Chris Vitale's resume/profile (used for auto-fill in production)
resume_info = {
    "name": "Chris Vitale",
    "email": "vitalechris32@gmail.com",
    "location": "Myrtle Beach, SC",
    "linkedin": "https://www.linkedin.com/in/chris-vitale-ou/",
    "resume_file": "Chris_Vitale_Resume_March_2025.pdf"
}

# List of job boards
job_boards = [
    {"name": "Indeed", "url": "https://www.indeed.com"},
    {"name": "Robert Half", "url": "https://www.roberthalf.com"},
    {"name": "Kforce", "url": "https://www.kforce.com"},
    {"name": "Insight Global", "url": "https://www.insightglobal.com"},
    {"name": "eFinancialCareers", "url": "https://www.efinancialcareers.com"},
    {"name": "CareerBuilder", "url": "https://www.careerbuilder.com"},
    {"name": "Glassdoor", "url": "https://www.glassdoor.com"},
    {"name": "Monster", "url": "https://www.monster.com"},
    {"name": "ZipRecruiter", "url": "https://www.ziprecruiter.com"},
    {"name": "Ladders", "url": "https://www.theladders.com"},
    {"name": "Hired", "url": "https://hired.com"},
    {"name": "Dice", "url": "https://www.dice.com"},
    {"name": "Builtin", "url": "https://builtin.com"},
    {"name": "Toptal", "url": "https://www.toptal.com"},
    {"name": "WayUp", "url": "https://www.wayup.com"},
    {"name": "Scouted", "url": "https://scouted.io"},
    {"name": "Wellfound (AngelList)", "url": "https://wellfound.com"},
    {"name": "Remote OK", "url": "https://remoteok.com"},
    {"name": "We Work Remotely", "url": "https://weworkremotely.com"},
    {"name": "FlexJobs", "url": "https://www.flexjobs.com"},
    {"name": "Working Nomads", "url": "https://www.workingnomads.co/jobs"},
    {"name": "Jobspresso", "url": "https://jobspresso.co"},
    {"name": "Remotive", "url": "https://remotive.io"},
    {"name": "SimplyHired", "url": "https://www.simplyhired.com"},
    {"name": "Snagajob", "url": "https://www.snagajob.com"},
    {"name": "Jooble", "url": "https://jooble.org"},
    {"name": "The Muse", "url": "https://www.themuse.com"},
    {"name": "Greenhouse", "url": "https://www.greenhouse.io"},
    {"name": "Lever", "url": "https://www.lever.co/jobs"},
    {"name": "Workday", "url": "https://www.myworkdayjobs.com"},
    {"name": "SmartRecruiters", "url": "https://www.smartrecruiters.com"},
    {"name": "Handshake", "url": "https://joinhandshake.com"},
    {"name": "Remote.co", "url": "https://remote.co/remote-jobs"},
    {"name": "SkipTheDrive", "url": "https://www.skipthedrive.com"},
    {"name": "Virtual Vocations", "url": "https://www.virtualvocations.com"}
]

# Simulated scraper (replace with real HTTP scraping or Selenium logic)
def scrape_jobs(keyword, location):
    time.sleep(2)  # simulate scraping
    return pd.DataFrame([
        {"Job Title": "Financial Analyst", "Company": "Kforce", "Location": location, "Link": "https://www.kforce.com/jobs"},
        {"Job Title": "Sr Financial Analyst", "Company": "Robert Half", "Location": location, "Link": "https://www.roberthalf.com/jobs"},
        {"Job Title": "FP&A Analyst", "Company": "Insight Global", "Location": location, "Link": "https://www.insightglobal.com/jobs"},
        {"Job Title": "Financial Analyst", "Company": "Indeed", "Location": location, "Link": "https://www.indeed.com/jobs"}
    ])

# Sidebar UI
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1077/1077012.png", width=80)
    st.title("👤 Chris Vitale")
    st.markdown(f"📍 {resume_info['location']}")
    st.markdown(f"✉️ {resume_info['email']}")
    st.markdown(f"[🔗 LinkedIn]({resume_info['linkedin']})", unsafe_allow_html=True)
    st.markdown("---")

    st.header("🔍 Filters")
    keyword = st.text_input("Keywords", "financial analyst")
    location = st.selectbox("Location", ["Orlando, FL", "Remote", "Hybrid"])
    test_mode = st.checkbox("🧪 Test mode", value=True)
    selected_boards = st.multiselect("Select job boards", [b["name"] for b in job_boards], default=["Indeed", "Robert Half", "Kforce", "Insight Global"])
    run_button = st.button("🚀 Run Job Search")

# Main Panel
st.title("📊 Finance Job Scraper + Auto Apply")
st.markdown("Scrapes 50+ finance job boards and applies using Chris Vitale's resume.")

if run_button:
    with st.spinner("Scraping selected job boards..."):
        jobs_df = scrape_jobs(keyword, location)

    st.success(f"Found {len(jobs_df)} job(s)")
    st.dataframe(jobs_df)

    st.subheader("📬 Apply to Jobs")
    for _, job in jobs_df.iterrows():
        with st.expander(f"{job['Job Title']} at {job['Company']} – {job['Location']}"):
            st.markdown(f"🔗 [Apply Here]({job['Link']})")
            if test_mode:
                st.info("Test mode: application not submitted")
            else:
                st.success("✅ Application submitted (simulated)")

else:
    st.info("Click 'Run Job Search' in the sidebar to start scraping.")
