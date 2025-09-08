import streamlit as st

st.set_page_config(page_title="Automated Blood Smear Analysis", page_icon="🧫", layout="wide")

st.title("Automated Blood Smear Analysis")
st.info(
    "This repository primarily contains a React (Vite) frontend and a Node/Express backend.\n\n"
    "This minimal Streamlit page is provided for Streamlit Cloud deployment only."
)

st.subheader("Project Links")
st.markdown("- Frontend (local dev): http://localhost:5173")
st.markdown("- Backend health (local dev): http://localhost:4004/api/health")

st.write(
    "If you intended to build a Python-based Streamlit app here, replace this file with your"
    " own Streamlit implementation and update requirements as needed."
)


