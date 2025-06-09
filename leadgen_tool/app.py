
import streamlit as st
import pandas as pd
from scraper import enrich_company_data
from scorer import score_leads

st.title("Smart Lead Scoring Tool")

uploaded_file = st.file_uploader("Upload CSV with 'Company' and 'Website' columns", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    enriched_df = enrich_company_data(df)
    final_df = score_leads(enriched_df)
    st.success("Leads enriched and scored!")
    st.dataframe(final_df)
    st.download_button("Download Scored Leads", final_df.to_csv(index=False), "scored_leads.csv")
