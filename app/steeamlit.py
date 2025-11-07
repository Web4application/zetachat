import streamlit as st
import time
from random import choice, randint
import sqlite3
import os

# ======================================================
# 🎨 Dark Theme CSS (unique from Facebook)
# ======================================================
dark_style = """
body {
    background-color: #121212;
    color: #e0e0e0;
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}
h1, h2, h3, h4, h5, h6 { color: #ffffff; }
.stApp { background-color: #121212; }
.stSidebar { background-color: #1f1f1f !important; color: #e0e0e0 !important; }
div.stButton > button {
    background-color: #4e5bdc; color: white; border: none; border-radius: 6px; padding: 0.5rem 1.2rem;
}
div.stButton > button:hover { background-color: #3a43a5; }
.stTextInput>div>div>input, .stTextArea textarea { background-color: #1f1f1f; color: #e0e0e0; border-radius:6px; }
.feed-card { background-color: #1f1f1f; border-radius:10px; padding:1rem; margin-bottom:1.5rem; }
.comment-reply { background-color:#2a2a2a; color:#b0b0b0; border-left:3px solid #4e5bdc; padding:0.4rem 0.8rem; margin:0.3rem 0; border-radius:4px;}
a { color: #6fa8dc; text-decoration:none; } a:hover { text-decoration: underline; }
"""

st.markdown(f"<style>{dark_style}</style>", unsafe_allow_html=True)

# ======================================================
# 🗄️ SQLite Setup (all modules internally)
# ======================================================
DB_FILE = "zetachat.db"
conn = sqlite3.connect(DB_FILE, check_same_thread=False)
c = conn.cursor()

# Users table
c.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    avatar TEXT,
    bio TEXT
)""")
# Posts table
c.execute("""CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    content TEXT,
    image TEXT,
    likes INTEGER,
    time TEXT
)""")
# Messages table
c.execute("""CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT,
    receiver TEXT,
    message TEXT,
    time TEXT
)""")
# Notifications table
c.execute("""CREATE TABLE IF NOT EXISTS notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    message TEXT,
    time TEXT
)""")
conn.commit()

# ======================================================
# 🧠 Helper Functions
# ======================================================
def login_user(username, password):
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    row = c.fetchone()
    return row and row[0]==password

def signup_user(username, password):
    c.execute("SELECT username FROM users WHERE username=?", (username,))
    if c.fetchone():
        return False
    avatar = f"https://i.pravatar.cc/50?img={randint(1,70)}"
    c.execute("INSERT INTO users (username,password,avatar,bio) VALUES (?,?,?,?)",
              (username,password,avatar,"New user bio"))
    conn.commit()
    return True

def get_user(username):
    c.execute("SELECT username, avatar, bio FROM users WHERE username=?", (username,))
    row = c.fetchone()
    if not row:
        return {}
    return {"username": row[0], "avatar": row[1], "bio": row[2]}

def create_post(user, content, image=None):
    c.execute("INSERT INTO posts (user, content, image, likes, time) VALUES (?,?,?,?,?)",
              (user, content, image if image else "", 0, time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

def get_posts():
    c.execute("SELECT user, content, image, likes, time FROM posts ORDER BY id DESC")
    return [{"user": r[0], "content": r[1], "image": r[2], "likes": r[3], "time": r[4], "comments":[]}
            for r in c.fetchall()]

def send_message(sender, receiver, message):
    c.execute("INSERT INTO messages (sender, receiver, message, time) VALUES (?,?,?,?)",
              (sender, receiver, message, time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

def get_messages(user1, user2):
    c.execute("""SELECT sender,message,time FROM messages
                 WHERE (sender=? AND receiver=?) OR (sender=? AND receiver=?)
                 ORDER BY id ASC""",(user1,user2,user2,user1))
    return [{"sender": r[0], "message": r[1], "time": r[2]} for r in c.fetchall()]

def add_notification(user, message):
    c.execute("INSERT INTO notifications (user,message,time) VALUES (?,?,?)",
              (user,message,time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

def get_notifications(user):
    c.execute("SELECT message FROM notifications WHERE user=? ORDER BY id DESC",(user,))
    return [r[0] for r in c.fetchall()]

# ======================================================
# 🌐 App Pages
# ======================================================
st.set_page_config(page_title="Zeta Chat", layout="wide")

if "page" not in st.session_state: st.session_state.page="login"
if "current_user" not in st.session_state: st.session_state.current_user=None

# ------------------ LOGIN / SIGNUP ------------------
if st.session_state.page=="login":
    st.title("Zeta Chat")
    st.subheader("Login")
    login_user_input = st.text_input("Username", key="login_user")
    login_pass_input = st.text_input("Password", type="password", key="login_pass")
    if st.button("Login"):
        if login_user(login_user_input, login_pass_input):
            st.session_state.current_user = login_user_input
            st.session_state.page="feed"
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")
    st.subheader("Signup")
    signup_user_input = st.text_input("New Username", key="signup_user")
    signup_pass_input = st.text_input("New Password", type="password", key="signup_pass")
    if st.button("Signup"):
        if signup_user(signup_user_input, signup_pass_input):
            st.success("Account created! Please login.")
        else:
            st.error("Username exists.")

# ------------------ MAIN FEED ------------------
elif st.session_state.page=="feed":
    user = get_user(st.session_state.current_user)
    st.sidebar.header(f"{user['username']}'s Profile")
    st.sidebar.image(user["avatar"])
    st.sidebar.markdown(f"**Bio:** {user['bio']}")
    if st.sidebar.button("Logout"):
        st.session_state.current_user=None
        st.session_state.page="login"
        st.experimental_rerun()

    st.subheader("Create Post")
    post_content = st.text_area("What's on your mind?")
    post_image = st.text_input("Image URL (optional)")
    if st.button("Post"):
        if post_content.strip()!="":
            create_post(user["username"], post_content, post_image)
            add_notification(user["username"], "You posted a new status!")
            st.success("Posted!")

    st.subheader("News Feed")
    for idx, post in enumerate(get_posts()):
        with st.container():
            st.markdown(f"<div class='feed-card'>", unsafe_allow_html=True)
            col1,col2=st.columns([1,5])
            with col1: st.image(get_user(post['user'])['avatar'], width=50)
            with col2:
                st.markdown(f"**{post['user']}** • {post['time']}")
                st.write(post['content'])
                if post['image']: st.image(post['image'])
            st.markdown(f"**Likes:** {post['likes']}  **Comments:** {len(post['comments'])}")
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("---")
