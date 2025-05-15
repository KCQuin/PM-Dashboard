import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter

st.title("📊 Task Analytics")

@st.cache_data
def load_data():
    # Placeholder for real data loading
    return pd.DataFrame()

# Load data
df = load_data()

if df.empty:
    st.warning("No data to display.")
else:
    st.subheader("Top Task Words")
    all_words = [word for sublist in df['task_wo_punct_split_wo_stopwords_lemmatized'] for word in sublist]
    word_counts = Counter(all_words).most_common(20)

    if word_counts:
        word_df = pd.DataFrame(word_counts, columns=['Word', 'Count'])
        fig = px.bar(word_df, x='Word', y='Count', color='Count')
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Hours by Project")
    project_hours = df.groupby("project")["hours"].sum().reset_index()
    fig2 = px.bar(project_hours, x="project", y="hours", color='hours')
    st.plotly_chart(fig2, use_container_width=True)
