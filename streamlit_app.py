import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
import base64

# Load cleaned combined data
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_combined_projects.csv")

df = load_data()

# Set Streamlit config
st.set_page_config(page_title="📊 Task Dashboard", layout="wide")

# Custom dark theme
st.markdown("""
    <style>
        body { background-color: #111; color: #eee; }
        .stApp { background-color: #1a1a1a; }
        h1, h2, h3, .stTextInput label, .stSelectbox label, .stSlider label { color: #90ee90; }
        .stSidebar { background-color: #222 !important; }
    </style>
""", unsafe_allow_html=True)

# Sidebar filters
st.sidebar.title("🔍 Filters")
project_options = df['Project'].unique()
projects = st.sidebar.multiselect("Select Project", project_options, default=project_options)
users = st.sidebar.multiselect("Select User", df['user_first_name'].unique())
search_term = st.sidebar.text_input("Search Task")

filtered_df = df[df['Project'].isin(projects)]
if users:
    filtered_df = filtered_df[filtered_df['user_first_name'].isin(users)]
if search_term:
    filtered_df = filtered_df[filtered_df['task'].str.contains(search_term, case=False, na=False)]

# Tabs
tab1, tab2, tab3 = st.tabs(["📄 Overview", "📊 Analytics", "📤 Export"])

with tab1:
    st.header("📄 Task Summary")
    st.dataframe(filtered_df, use_container_width=True)

with tab2:
    st.header("📊 Most Common Words")
    all_words = [word for sublist in filtered_df['task_lemmas'].dropna().apply(eval) for word in sublist]
    word_counts = Counter(all_words).most_common(20)
    if word_counts:
        word_df = pd.DataFrame(word_counts, columns=['Word', 'Count'])
        fig = px.bar(word_df, x='Word', y='Count', color='Count', color_continuous_scale='Greens')
        fig.update_layout(paper_bgcolor='#1a1a1a', font_color='#eee')
        st.plotly_chart(fig, use_container_width=True)

    st.header("📅 Hours by Project")
    if 'minutes' in filtered_df.columns:
        filtered_df['Hours'] = filtered_df['minutes'] / 60
        project_hours = filtered_df.groupby("Project")['Hours'].sum().reset_index()
        fig2 = px.bar(project_hours, x='Project', y='Hours', color='Hours', color_continuous_scale='Greens')
        fig2.update_layout(paper_bgcolor='#1a1a1a', font_color='#eee')
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("Minutes column not found to compute hours.")

with tab3:
    st.header("📤 Download Cleaned Data")
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download CSV", csv_data, "filtered_tasks.csv", "text/csv")

st.caption("\u2728 Dashboard by Kristal | Theme: Dark Green & Grayscale")
