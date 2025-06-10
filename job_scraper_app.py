import streamlit as st
import pandas as pd
import time

# Placeholder for actual scraping logic
def scrape_jobs():
    # Simulated job data
    data = [
        {"Job Title": "Financial Analyst", "Company": "Company A", "Location": "Orlando, FL", "Link": "https://example.com/apply1"},
        {"Job Title": "Remote Financial Analyst", "Company": "Company B", "Location": "Remote", "Link": "https://example.com/apply2"},
        {"Job Title": "Senior Financial Analyst", "Company": "Company C", "Location": "Orlando, FL", "Link": "https://example.com/apply3"},
    ]
    return pd.DataFrame(data)

# Page config
st.set_page_config(page_title="Job Scraper App", page_icon="📈", layout="wide")

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1077/1077012.png", width=80)
    st.title("👤 Chris Vitale")
    st.markdown("**Location:** Myrtle Beach, SC")
    st.markdown("**Email:** vitalechris32@gmail.com")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/chris-vitale-ou/)")
    test_mode = st.checkbox("🧪 Test Mode", value=True)
    custom_keyword = st.text_input("🔍 Keywords", "financial analyst")
    run_scraper = st.button("🚀 Run Job Search")

# Main app
st.title("📊 Financial Analyst Job Scraper Dashboard")
st.markdown("This app searches *Indeed, Robert Half, Insight Global, Kforce,* and *LinkedIn* for remote or Orlando-based Financial Analyst jobs.")

if run_scraper:
    with st.spinner("Scraping job boards... Please wait."):
        time.sleep(2)  # Simulate scraping delay
        jobs_df = scrape_jobs()
        st.success(f"✅ Found {len(jobs_df)} jobs!")

        col1, col2 = st.columns([3, 2])

        with col1:
            st.subheader("📄 Job Listings")
            st.dataframe(jobs_df)

        with col2:
            st.subheader("📬 Apply Panel")
            for _, row in jobs_df.iterrows():
                st.markdown(f"**{row['Job Title']}** at *{row['Company']}* - {row['Location']}")
                st.markdown(f"[Apply Here]({row['Link']})", unsafe_allow_html=True)
                if not test_mode:
                    st.success("Applied successfully!")
                else:
                    st.info("Test Mode: Skipped real application")
else:
    st.info("Click 'Run Job Search' in the sidebar to begin.")
