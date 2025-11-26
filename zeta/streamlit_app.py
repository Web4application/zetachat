import streamlit as st
import os

# Load global CSS
with open("assets/dark_style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Redirect to Welcome page
st.experimental_set_query_params(page="welcome")
st.experimental_rerun()
