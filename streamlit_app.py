import streamlit as st
import time
from random import choice, randint
import os

# ======================================================
# 🎨 Zeta Dark CSS
# ======================================================
zeta_dark_css = """
body { background-color: #1c1f26; color: #e0e0e0; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
h1,h2,h3,h4 { color: #ffffff; font-weight: 700; }
.stSidebar { background-color: #22252d !important; color: #e0e0e0 !important; border-right: 2px solid #2f3136; padding: 1rem; }
div.stButton > button { background-color: #5a6cff; color: white; border: none; border-radius: 8px; padding: 0.6rem 1.5rem; font-weight: 600; transition: all 0.2s ease-in-out; }
div.stButton > button:hover { background-color: #4048c0; transform: scale(1.05); }
.stTextInput > div > div > input, .stTextArea textarea { background-color: #2a2d36; color: #ffffff; border: 1px solid #444753; border-radius: 8px; padding: 0.5rem; }
.stTextInput > div > div > input:focus, .stTextArea textarea:focus { border: 1px solid #5a6cff; outline: none; }
.nav-bar { display: flex; justify-content: space-around; background-color: #1f222b; padding: 0.5rem; border-bottom: 2px solid #2f3136; margin-bottom: 1rem; }
.nav-bar button { background-color: transparent; border: none; color: #e0e0e0; font-weight: 600; padding: 0.5rem 1rem; transition: color 0.2s ease-in-out; cursor: pointer; }
.nav-bar button:hover { color: #5a6cff; transform: scale(1.05); }
.feed-card { background-color: #2a2d36; border-radius: 12px; padding: 1rem; box-shadow: 0 4px 15px rgba(0,0,0,0.4); margin-bottom: 1.5rem; transition: transform 0.15s ease; }
.feed-card:hover { transform: translateY(-2px) scale(1.01); }
.comment-reply { background-color: #1f222b; color: #c0c0c0; border-left: 3px solid #5a6cff; padding: 0.4rem 0.8rem; margin: 0.3rem 0; border-radius: 6px; }
.chat-bubble { padding: 0.5rem 1rem; border-radius: 12px; margin: 0.3rem 0; max-width: 70%; }
.chat-bubble.user { background-color: #5a6cff; color: #ffffff; align-self: flex-end; }
.chat-bubble.friend { background-color: #3b3f4c; color: #ffffff; align-self: flex-start; }
::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-thumb { background-color: #5a6cff; border-radius: 10px; }
::-webkit-scrollbar-track { background: #1c1f26; }
.friend-request-card { background-color: #2a2d36; border-radius: 10px; padding: 0.6rem; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center; }
.notification-card { background-color: #2a2d36; border-radius: 8px; padding: 0.6rem; margin-bottom: 0.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.3); }
"""
# Save CSS file if it doesn't exist
if not os.path.exists("zeta_dark.css"):
    with open("zeta_dark.css", "w") as f:
        f.write(zeta_dark_css)
# Load CSS
with open("zeta_dark.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======================================================
# 🧠 Mock Database
# ======================================================
if "users" not in st.session_state:
    st.session_state.users = {
        "admin": {"password":"password","avatar":"https://i.pravatar.cc/50?img=1","bio":"Hello! I'm admin.","friends":["user1"],"requests":[]},
        "user1": {"password":"1234","avatar":"https://i.pravatar.cc/50?img=2","bio":"I am user1.","friends":["admin"],"requests":[]}
    }
if "current_user" not in st.session_state: st.session_state.current_user = None
if "posts" not in st.session_state: st.session_state.posts = []
if "notifications" not in st.session_state: st.session_state.notifications = []
if "chats" not in st.session_state: st.session_state.chats = {}

sample_images = ["https://picsum.photos/400/200?random=1","https://picsum.photos/400/200?random=2",
                 "https://picsum.photos/400/200?random=3","https://picsum.photos/400/200?random=4"]

# ======================================================
# 🔐 Auth Functions
# ======================================================
def login(username,password):
    if username in st.session_state.users and st.session_state.users[username]["password"] == password:
        st.session_state.current_user = username
        st.success(f"Logged in as {username}")
    else: st.error("Invalid username or password")

def signup(username,password):
    if username in st.session_state.users: st.error("Username already exists")
    else:
        avatar_url=f"https://i.pravatar.cc/50?img={randint(5,70)}"
        st.session_state.users[username] = {"password":password,"avatar":avatar_url,"bio":"New user bio","friends":[],"requests":[]}
        st.success("Account created! Please log in.")

# ======================================================
# 🌐 Navigation
# ======================================================
st.set_page_config(page_title="Zeta Chat", layout="wide")

if st.session_state.current_user is None:
    st.title("Zeta Chat")
    page = st.radio("Select Page", ["Login","Signup","Forgot Password"])
else:
    page = st.radio("Select Page", ["Feed","Chat","Friends","Notifications","Profile","Logout"])

# ======================================================
# 🔑 Pages
# ======================================================

# ---------- Auth Pages ----------
if page == "Login":
    st.subheader("Login")
    login_user = st.text_input("Username", key="login_user")
    login_pass = st.text_input("Password", type="password", key="login_pass")
    if st.button("Login"): login(login_user, login_pass)

elif page == "Signup":
    st.subheader("Signup")
    signup_user = st.text_input("New Username", key="signup_user")
    signup_pass = st.text_input("New Password", type="password", key="signup_pass")
    if st.button("Signup"): signup(signup_user, signup_pass)

elif page == "Forgot Password":
    st.subheader("Forgot Password")
    st.text("Feature coming soon...")

# ---------- Main App ----------
elif page == "Feed":
    st.subheader("📰 News Feed")
    for idx, post in enumerate(st.session_state.posts):
        with st.container():
            st.markdown(f"<div class='feed-card'>", unsafe_allow_html=True)
            col1,col2 = st.columns([1,5])
            with col1: st.image(post["avatar"],width=50)
            with col2:
                st.markdown(f"**{post['user']}**  •  {post['time']}")
                st.write(post["content"])
                if post["image"]: st.image(post["image"])
            st.markdown(f"**Likes:** {post['likes']}   **Comments:** {len(post['comments'])}   **Shares:** {post['shares']}")
            for c in post['comments']:
                st.markdown(f"<div class='comment-reply'>{c}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("---")
    # Post creation
    st.subheader("Create a Post")
    post_text = st.text_area("What's on your mind?")
    post_image_url = st.text_input("Image URL (optional)")
    if st.button("Post"):
        if post_text.strip()!="":
            post = {"user":st.session_state.current_user,"avatar":st.session_state.users[st.session_state.current_user]["avatar"],
                    "content":post_text,"image":post_image_url if post_image_url else choice(sample_images),
                    "likes":0,"comments":[],"shares":0,"time":time.strftime("%Y-%m-%d %H:%M:%S")}
            st.session_state.posts.insert(0,post)
            st.success("Posted!")

# ---------- Chat ----------
elif page == "Chat":
    st.subheader("💬 Chat")
    chat_with = st.selectbox("Select Friend", [""]+[f for f in st.session_state.users if f!=st.session_state.current_user])
    if chat_with:
        chat_key = tuple(sorted([st.session_state.current_user, chat_with]))
        if chat_key not in st.session_state.chats: st.session_state.chats[chat_key] = []
        chat_messages = st.session_state.chats[chat_key]
        for msg in chat_messages:
            st.markdown(f"<div class='chat-bubble {msg['sender']}'>{msg['message']}</div>", unsafe_allow_html=True)
        new_msg = st.text_input("Type a message")
        if st.button("Send"):
            chat_messages.append({"sender":"user","message":new_msg})
            st.experimental_rerun()

# ---------- Friends ----------
elif page == "Friends":
    st.subheader("👥 Friends")
    user = st.session_state.users[st.session_state.current_user]
    for f in user["friends"]:
        st.markdown(f"- {f}")
    st.subheader("Friend Requests")
    for req in user["requests"]:
        col1,col2 = st.columns([2,1])
        col1.markdown(f"Friend request from **{req}**")
        if col2.button(f"Accept {req}"):
            user["friends"].append(req)
            st.session_state.users[req]["friends"].append(st.session_state.current_user)
            user["requests"].remove(req)
            st.success(f"You are now friends with {req}")

# ---------- Notifications ----------
elif page == "Notifications":
    st.subheader("🔔 Notifications")
    for n in st.session_state.notifications[::-1]:
        st.markdown(f"<div class='notification-card'>{n}</div>", unsafe_allow_html=True)

# ---------- Profile ----------
elif page == "Profile":
    st.subheader(f"{st.session_state.current_user}'s Profile")
    user = st.session_state.users[st.session_state.current_user]
    st.image(user["avatar"])
    st.text_area("Bio", value=user["bio"])
    st.text("Posts")
    for post in st.session_state.posts:
        if post["user"] == st.session_state.current_user: st.write(post["content"])

# ---------- Logout ----------
elif page == "Logout":
    st.session_state.current_user = None
    st.experimental_rerun()

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
