import streamlit as st

st.title("👋 Welcome to ZetaChat")
st.write("Your Facebook-style experience, fully dark-themed and modern.")

col1, col2 = st.columns(2)
with col1:
    if st.button("Login"):
        st.experimental_set_query_params(page="login")
        st.experimental_rerun()
with col2:
    if st.button("Sign Up"):
        st.experimental_set_query_params(page="signup")
        st.experimental_rerun()
