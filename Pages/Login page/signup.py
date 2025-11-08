import streamlit as st
from random import randint

if "users" not in st.session_state:
    st.session_state.users = {}

st.title("📝 Sign Up")

full_name = st.text_input("Full Name")
email = st.text_input("Email")
age = st.number_input("Age", min_value=1, max_value=120)
country = st.text_input("Country")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
password = st.text_input("Password", type="password")

if st.button("Sign Up"):
    if email in st.session_state.users:
        st.error("Email already registered.")
    else:
        st.session_state.users[email] = {
            "name": full_name,
            "email": email,
            "age": age,
            "country": country,
            "gender": gender,
            "password": password,
            "avatar": f"https://i.pravatar.cc/50?img={randint(1,70)}",
            "bio": "Hello! I'm new to ZetaChat.",
            "friends": [],
            "posts": []
        }
        st.success("Account created! Please login.")
        st.experimental_set_query_params(page="login")
        st.experimental_rerun()
