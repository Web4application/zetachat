import streamlit as st
from random import choice, randint
import time

# ======================================================
# Load Dark CSS
# ======================================================
with open("assets/dark_style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Dark mode CSS directly in the app
dark_css = """
body {
    background-color: #121212;
    color: #e0e0e0;
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}

h1, h2, h3, h4, h5, h6 {
    color: #ffffff;
}

/* Buttons */
div.stButton > button {
    background-color: #1e88e5;
    color: white;
    border-radius: 8px;
}
div.stButton > button:hover {
    background-color: #1565c0;
}

/* Inputs */
.stTextInput > div > div > input, .stTextArea textarea {
    background-color: #1c1c1c;
    color: #e0e0e0;
    border-radius: 6px;
    border: 1px solid #333;
}

/* Feed Cards */
.feed-card {
    background-color: #1e1e1e;
    padding: 1rem;
    border-radius: 10px;
    box-shadow: 0 0 5px rgba(0,0,0,0.3);
}
.comment-reply {
    background-color: #2a2a2a;
    padding: 0.5rem;
    border-left: 3px solid #1e88e5;
    margin: 0.3rem 0;
    border-radius: 4px;
}
"""

# Inject CSS
st.markdown(f"<style>{dark_css}</style>", unsafe_allow_html=True)

# ======================================================
# Initialize Session State
# ======================================================
if "users" not in st.session_state:
    st.session_state.users = {
        "admin": {"password": "admin123", "avatar": f"https://i.pravatar.cc/50?img=1", "bio": "Admin user", "friends": [], "requests": []}
    }

if "current_user" not in st.session_state:
    st.session_state.current_user = None

if "posts" not in st.session_state:
    st.session_state.posts = []

if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_page" not in st.session_state:
    st.session_state.current_page = "login"

sample_images = [
    "https://picsum.photos/400/200?random=1",
    "https://picsum.photos/400/200?random=2"
]

# ======================================================
# Auth Functions
# ======================================================
def login(username, password):
    users = st.session_state.users
    if username in users and users[username]["password"] == password:
        st.session_state.current_user = username
        st.session_state.current_page = "feed"
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

# ======================================================
# Navigation
# ======================================================
def set_page(page_name):
    st.session_state.current_page = page_name

# ======================================================
# Login Page
# ======================================================
if st.session_state.current_user is None or st.session_state.current_page == "login":
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

# ======================================================
# Main App Navigation
# ======================================================
else:
    user = st.session_state.users[st.session_state.current_user]

    # Top Navigation Bar
    col_feed, col_profile, col_chat, col_logout = st.columns([1,1,1,1])
    with col_feed:
        if st.button("📰 Feed"):
            set_page("feed")
    with col_profile:
        if st.button("👤 Profile"):
            set_page("profile")
    with col_chat:
        if st.button("💬 Chat"):
            set_page("chat")
    with col_logout:
        if st.button("🚪 Logout"):
            st.session_state.current_user = None
            st.session_state.current_page = "login"
            st.experimental_rerun()

    st.markdown("---")

    # ==================================================
    # Feed Page
    # ==================================================
    if st.session_state.current_page == "feed":
        st.subheader("📰 Feed")
        post_text = st.text_area("What's on your mind?")
        post_image_url = st.text_input("Image URL (optional)")

        if st.button("Post"):
            if post_text.strip() != "":
                post = {
                    "user": st.session_state.current_user,
                    "avatar": user["avatar"],
                    "content": post_text,
                    "image": post_image_url if post_image_url else choice(sample_images),
                    "likes": 0,
                    "comments": [],
                    "shares": 0,
                    "time": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.posts.insert(0, post)
                st.success("Posted!")

        for idx, post in enumerate(st.session_state.posts):
            if post["user"] != st.session_state.current_user and post["user"] not in user["friends"]:
                continue
            st.markdown(f"**{post['user']}** • {post['time']}")
            st.write(post["content"])
            if post["image"]:
                st.image(post["image"])

    # ==================================================
    # Profile Page
    # ==================================================
    elif st.session_state.current_page == "profile":
        st.subheader("👤 Profile")
        st.image(user["avatar"])
        st.markdown(f"**Bio:** {user['bio']}")

        st.subheader("Friends")
        for f in user["friends"]:
            st.markdown(f"- {f}")

        st.subheader("Friend Requests")
        for req in user["requests"]:
            col1, col2 = st.columns([2,1])
            col1.markdown(f"{req} wants to be your friend")
            if col2.button(f"Accept {req}"):
                user["friends"].append(req)
                st.session_state.users[req]["friends"].append(st.session_state.current_user)
                user["requests"].remove(req)
                st.experimental_rerun()

    # ==================================================
    # Chat Page
    # ==================================================
    elif st.session_state.current_page == "chat":
        st.subheader("💬 Chat")
        if not user["friends"]:
            st.info("Add friends to start chatting!")
        else:
            chat_user = st.selectbox("Chat with:", [""] + user["friends"])
            if chat_user:
                msg_input = st.text_input("Type your message", key=f"chat_{chat_user}")
                if st.button("Send", key=f"send_{chat_user}") and msg_input.strip():
                    st.session_state.messages.append(f"{st.session_state.current_user} → {chat_user}: {msg_input}")
                    st.experimental_rerun()
                st.subheader("Messages")
                for msg in st.session_state.messages:
                    if chat_user in msg:
                        st.markdown(msg)
