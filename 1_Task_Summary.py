import streamlit as st
import pandas as pd

st.title("🗂️ Task Summary")

@st.cache_data
def load_data():
    # Placeholder for real data loading
    return pd.DataFrame()

# Load data
df = load_data()

if df.empty:
    st.warning("No data available.")
else:
    st.sidebar.header("Filters")
    projects = st.sidebar.multiselect("Filter by Project", df['project'].unique())
    names = st.sidebar.multiselect("Filter by User", df['full_name'].unique())

    filtered_df = df.copy()
    if projects:
        filtered_df = filtered_df[filtered_df['project'].isin(projects)]
    if names:
        filtered_df = filtered_df[filtered_df['full_name'].isin(names)]

    st.dataframe(filtered_df.head(100), use_container_width=True)
