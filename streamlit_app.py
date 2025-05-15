import streamlit as st
from PIL import Image

st.set_page_config(page_title="Task Dashboard Home", layout="wide")

# Sidebar
st.sidebar.title("📁 Navigation")
st.sidebar.success("Select a page from the left menu")

# Main content
st.title("🚀 Welcome to the Project Task Dashboard")

st.markdown("""
This dashboard allows you to:
- 📊 Analyze team productivity and task patterns
- 🧠 Extract common keywords from task logs
- 🗓️ View activity trends over time
- 📤 Upload or export data files

Built with ❤️ using Streamlit.
""")

st.info("Use the sidebar to navigate between different sections.")
