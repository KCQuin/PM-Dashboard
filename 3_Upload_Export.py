import streamlit as st
import pandas as pd
import base64

st.title("📤 Upload & Export")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success(f"Uploaded {uploaded_file.name} with {df.shape[0]} rows.")
    st.dataframe(df.head())

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download as CSV", csv, file_name="export.csv", mime="text/csv")
else:
    st.info("Upload a CSV file to preview and download.")
