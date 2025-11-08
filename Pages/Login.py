import streamlit as st

if "users" not in st.session_state:
    st.session_state.users = {}

st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = st.session_state.users.get(email)
    if user and user["password"] == password:
        st.session_state.current_user = email
        st.success("Login successful!")
        st.experimental_set_query_params(page="main_app")
        st.experimental_rerun()
    else:
        st.error("Invalid credentials.")
