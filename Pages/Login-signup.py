import streamlit as st
from random import randint

# Load CSS
with open("assets/dark_style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state
if "users" not in st.session_state:
    st.session_state.users = {
        "admin": {"password": "admin123", "avatar": f"https://i.pravatar.cc/50?img=1", "bio": "Admin user", "friends": [], "requests": []}
    }

if "current_user" not in st.session_state:
    st.session_state.current_user = None

# Auth functions
def login(username, password):
    users = st.session_state.users
    if username in users and users[username]["password"] == password:
        st.session_state.current_user = username
        st.success(f"Welcome, {username}!")
        st.experimental_rerun()
    else:
        st.error("Invalid username or password")

def signup(username, password):
    users = st.session_state.users
    if username in users:
        st.error("Username already exists")
    else:
        avatar_url = f"https://i.pravatar.cc/50?img={randint(2,70)}"
        users[username] = {"password": password, "avatar": avatar_url, "bio": "New user bio", "friends": [], "requests": []}
        st.success("Account created! Please log in.")

# Login Page
st.title("🔑 Zeta Chat Login")
login_user = st.text_input("Username")
login_pass = st.text_input("Password", type="password")

col1, col2 = st.columns(2)
with col1:
    if st.button("Login"):
        login(login_user, login_pass)
with col2:
    if st.button("Signup"):
        signup(login_user, login_pass)

st.markdown("---")
st.subheader("Forgot Password?")
st.text("Recovery link placeholder")
