import streamlit as st
import time
from random import choice, randint
import sqlite3
import toml
import os

# -------------------------------
# Load config
# -------------------------------
CONFIG_FILE = "config.toml"
if not os.path.exists(CONFIG_FILE):
    st.error("Config file not found. Please create config.toml")
    st.stop()

config = toml.load(CONFIG_FILE)

# -------------------------------
# Database setup (SQLite for local)
# -------------------------------
DB_PATH = config['database']['path']
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

# Users table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    avatar TEXT,
    bio TEXT
)
''')

# Messages table
c.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT,
    receiver TEXT,
    message TEXT,
    timestamp TEXT
)
''')

# Posts table
c.execute('''
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    content TEXT,
    image TEXT,
    likes INTEGER,
    comments TEXT,
    shares INTEGER,
    time TEXT
)
''')
conn.commit()

# -------------------------------
# Mock initial users if empty
# -------------------------------
c.execute("SELECT COUNT(*) FROM users")
if c.fetchone()[0] == 0:
    users = [
        ("admin", "password", "https://i.pravatar.cc/50?img=1", "Hello! I'm admin."),
        ("user1", "1234", "https://i.pravatar.cc/50?img=2", "I am user1.")
    ]
    c.executemany("INSERT INTO users VALUES (?,?,?,?)", users)
    conn.commit()

# -------------------------------
# Session state
# -------------------------------
if "current_user" not in st.session_state:
    st.session_state.current_user = None

if "page" not in st.session_state:
    st.session_state.page = "login"

# -------------------------------
# CSS (from config)
# -------------------------------
css = f"""
body {{
    background-color: {config['ui']['primary_color']};
    color: #fff;
    font-family: {config['ui']['font_family']};
}}
.stButton>button {{
    background-color: {config['ui']['accent_color']};
    color: white;
    border-radius: 6px;
    padding: 0.5rem 1.2rem;
}}
.stButton>button:hover {{
    background-color: {config['ui']['secondary_color']};
}}
.stTextInput>div>div>input, .stTextArea textarea {{
    background-color: {config['ui']['secondary_color']};
    color: white;
    border-radius: 6px;
}}
.feed-card {{
    background-color: {config['ui']['secondary_color']};
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 1rem;
}}
.comment-reply {{
    background-color: {config['ui']['primary_color']};
    color: #ccc;
    border-left: 3px solid {config['ui']['accent_color']};
    padding: 0.3rem 0.6rem;
    margin: 0.3rem 0;
    border-radius: 4px;
}}
"""
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# -------------------------------
# Authentication functions
# -------------------------------
def login(username, password):
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    row = c.fetchone()
    if row and row[0] == password:
        st.session_state.current_user = username
        st.session_state.page = "feed"
        st.success(f"Welcome {username}")
    else:
        st.error("Invalid username or password")

def signup(username, password):
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone():
        st.error("Username already exists")
    else:
        avatar = f"https://i.pravatar.cc/50?img={randint(3,70)}"
        bio = "New user bio"
        c.execute("INSERT INTO users VALUES (?,?,?,?)", (username, password, avatar, bio))
        conn.commit()
        st.success("Account created! Please log in.")

# -------------------------------
# Sidebar navigation
# -------------------------------
if st.session_state.current_user:
    st.sidebar.title("Navigation")
    if config['features']['feed']:
        if st.sidebar.button("Feed"):
            st.session_state.page = "feed"
    if config['features']['chat']:
        if st.sidebar.button("Chat"):
            st.session_state.page = "chat"
    if config['features']['friends']:
        if st.sidebar.button("Friends"):
            st.session_state.page = "friends"
    if config['features']['notifications']:
        if st.sidebar.button("Notifications"):
            st.session_state.page = "notifications"
    if st.sidebar.button("Logout"):
        st.session_state.current_user = None
        st.session_state.page = "login"
        st.experimental_rerun()

# -------------------------------
# Pages
# -------------------------------
def page_login():
    st.title(config['app']['name'])
    st.subheader("Login or Signup")
    col1, col2 = st.columns(2)
    with col1:
        st.text("Login")
        login_user = st.text_input("Username", key="login_user")
        login_pass = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            login(login_user, login_pass)
    with col2:
        st.text("Signup")
        signup_user = st.text_input("New Username", key="signup_user")
        signup_pass = st.text_input("New Password", type="password", key="signup_pass")
        if st.button("Signup"):
            signup(signup_user, signup_pass)

def page_feed():
    st.header("📰 News Feed")
    c.execute("SELECT * FROM posts ORDER BY id DESC LIMIT ?", (config['features.feed']['max_posts_display'],))
    posts = c.fetchall()
    for post in posts:
        st.markdown(f"<div class='feed-card'>", unsafe_allow_html=True)
        st.markdown(f"**{post[1]}**")
        st.write(post[2])
        if post[3]:
            st.image(post[3])
        st.markdown("</div>", unsafe_allow_html=True)

def page_chat():
    st.header("💬 Chat")
    c.execute("SELECT username FROM users WHERE username != ?", (st.session_state.current_user,))
    other_users = [row[0] for row in c.fetchall()]
    selected_user = st.selectbox("Select user to chat with", [""] + other_users)
    if selected_user:
        msg_input = st.text_input("Your message")
        if st.button("Send"):
            if msg_input.strip():
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                c.execute("INSERT INTO messages (sender, receiver, message, timestamp) VALUES (?,?,?,?)",
                          (st.session_state.current_user, selected_user, msg_input, timestamp))
                conn.commit()
                st.success("Message sent!")

        # Display conversation
        c.execute("""
        SELECT sender, message, timestamp FROM messages
        WHERE (sender=? AND receiver=?) OR (sender=? AND receiver=?)
        ORDER BY id ASC
        """, (st.session_state.current_user, selected_user, selected_user, st.session_state.current_user))
        conversation = c.fetchall()
        for m in conversation:
            align = "right" if m[0] == st.session_state.current_user else "left"
            st.markdown(f"<div style='text-align:{align};'>{m[0]}: {m[1]} <small>{m[2]}</small></div>", unsafe_allow_html=True)

def page_friends():
    st.header("👥 Friends")
    c.execute("SELECT username FROM users WHERE username != ?", (st.session_state.current_user,))
    users_list = [row[0] for row in c.fetchall()]
    st.write(users_list)

def page_notifications():
    st.header("🔔 Notifications")
    st.info("No real notifications yet (can integrate later).")

# -------------------------------
# Render page
# -------------------------------
if st.session_state.page == "login":
    page_login()
elif st.session_state.page == "feed":
    page_feed()
elif st.session_state.page == "chat":
    page_chat()
elif st.session_state.page == "friends":
    page_friends()
elif st.session_state.page == "notifications":
    page_notifications()

import streamlit as st
import toml
import os
import sqlite3
import time
from random import choice, randint

# -------------------- Config --------------------
CONFIG_FILE = "config.toml"
config = toml.load(CONFIG_FILE)

# -------------------- CSS --------------------
if os.path.exists("style.css"):
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------- SQLite DB --------------------
DB_PATH = config['database']['path']
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

# Users table
c.execute("""CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    avatar TEXT,
    bio TEXT
)""")
# Friends table
c.execute("""CREATE TABLE IF NOT EXISTS friends (
    user TEXT,
    friend TEXT
)""")
# Friend requests
c.execute("""CREATE TABLE IF NOT EXISTS requests (
    sender TEXT,
    receiver TEXT
)""")
# Posts table
c.execute("""CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    content TEXT,
    image TEXT,
    timestamp TEXT
)""")
# Messages table
c.execute("""CREATE TABLE IF NOT EXISTS messages (
    sender TEXT,
    receiver TEXT,
    message TEXT,
    timestamp TEXT
)""")
# Notifications table
c.execute("""CREATE TABLE IF NOT EXISTS notifications (
    user TEXT,
    content TEXT,
    timestamp TEXT
)""")
conn.commit()

# -------------------- Session State --------------------
if "current_user" not in st.session_state:
    st.session_state.current_user = None
if "page" not in st.session_state:
    st.session_state.page = "login"

# -------------------- Auth --------------------
def login(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if c.fetchone():
        st.session_state.current_user = username
        st.session_state.page = "feed"
        st.success(f"Logged in as {username}")
    else:
        st.error("Invalid username or password")

def signup(username, password):
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone():
        st.error("Username already exists")
    else:
        avatar_url = f"https://i.pravatar.cc/50?img={randint(1,70)}"
        c.execute("INSERT INTO users VALUES (?,?,?,?)", (username, password, avatar_url, "New user bio"))
        conn.commit()
        st.success("Account created! Please log in.")

# -------------------- Navigation --------------------
def nav_buttons():
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        if st.button("📰 Feed"):
            st.session_state.page = "feed"
            st.experimental_rerun()
    with col2:
        if st.button("💬 Chat"):
            st.session_state.page = "chat"
            st.experimental_rerun()
    with col3:
        if st.button("👥 Friends"):
            st.session_state.page = "friends"
            st.experimental_rerun()
    with col4:
        if st.button("🔔 Notifications"):
            st.session_state.page = "notifications"
            st.experimental_rerun()
    st.markdown("---")

# -------------------- App --------------------
st.set_page_config(page_title=config['app']['name'], layout="wide")
st.title(config['app']['name'])

if st.session_state.current_user is None:
    st.subheader("Login")
    login_user = st.text_input("Username", key="login_user")
    login_pass = st.text_input("Password", type="password", key="login_pass")
    if st.button("Login"):
        login(login_user, login_pass)

    st.subheader("Signup")
    signup_user = st.text_input("New Username", key="signup_user")
    signup_pass = st.text_input("New Password", type="password", key="signup_pass")
    if st.button("Signup"):
        signup(signup_user, signup_pass)

# -------------------- FEED --------------------
elif st.session_state.page == "feed":
    nav_buttons()
    st.subheader("📰 Feed")

    # Display posts
    c.execute("SELECT * FROM posts ORDER BY timestamp DESC LIMIT ?", (config['features']['feed']['max_posts_display'],))
    posts = c.fetchall()
    for post in posts:
        st.markdown(f"<div class='feed-card'>", unsafe_allow_html=True)
        st.markdown(f"**{post[1]}**  •  {post[4]}")
        st.write(post[2])
        if post[3]:
            st.image(post[3])
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("---")

    # Create post
    st.subheader("Create a Post")
    post_text = st.text_area("What's on your mind?")
    post_image = st.text_input("Image URL (optional)")
    if st.button("Post"):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        image = post_image if post_image else f"https://picsum.photos/400/200?random={randint(1,100)}"
        c.execute("INSERT INTO posts (user, content, image, timestamp) VALUES (?,?,?,?)",
                  (st.session_state.current_user, post_text, image, timestamp))
        c.execute("INSERT INTO notifications (user, content, timestamp) VALUES (?,?,?)",
                  (st.session_state.current_user, f"Posted a new status", timestamp))
        conn.commit()
        st.success("Posted!")
        st.experimental_rerun()

# -------------------- CHAT --------------------
elif st.session_state.page == "chat":
    nav_buttons()
    st.subheader("💬 Chat")
    user_list = [u[0] for u in c.execute("SELECT username FROM users WHERE username != ?", (st.session_state.current_user,)).fetchall()]
    chat_with = st.selectbox("Select a user to chat with", [""] + user_list)

    if chat_with:
        c.execute("""SELECT sender, message FROM messages 
                     WHERE (sender=? AND receiver=?) OR (sender=? AND receiver=?) 
                     ORDER BY rowid ASC""", 
                  (st.session_state.current_user, chat_with, chat_with, st.session_state.current_user))
        messages = c.fetchall()
        st.markdown("<div style='height:300px;overflow-y:auto;'>", unsafe_allow_html=True)
        for msg in messages:
            color = "#ff4b2b" if msg[0]==st.session_state.current_user else "#ffffff"
            align = "right" if msg[0]==st.session_state.current_user else "left"
            st.markdown(f"<div style='text-align:{align};color:{color};'>{msg[0]}: {msg[1]}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        new_msg = st.text_input("Type a message", key=f"input_{chat_with}")
        if st.button("Send", key=f"send_{chat_with}") and new_msg.strip():
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            c.execute("INSERT INTO messages VALUES (?,?,?,?)",
                      (st.session_state.current_user, chat_with, new_msg, timestamp))
            c.execute("INSERT INTO notifications VALUES (?,?,?)",
                      (chat_with, f"New message from {st.session_state.current_user}", timestamp))
            conn.commit()
            st.experimental_rerun()

# -------------------- FRIENDS --------------------
elif st.session_state.page == "friends":
    nav_buttons()
    st.subheader("👥 Friends")

    # List friends
    friends = [f[0] for f in c.execute("SELECT friend FROM friends WHERE user=?", (st.session_state.current_user,)).fetchall()]
    st.markdown("**Your Friends:**")
    for f in friends:
        st.write(f)

    # Friend requests
    st.markdown("**Friend Requests:**")
    requests = [r[0] for r in c.execute("SELECT sender FROM requests WHERE receiver=?", (st.session_state.current_user,)).fetchall()]
    for req in requests:
        col1, col2 = st.columns([2,1])
        col1.write(req)
        if col2.button(f"Accept {req}"):
            c.execute("INSERT INTO friends VALUES (?,?)", (st.session_state.current_user, req))
            c.execute("INSERT INTO friends VALUES (?,?)", (req, st.session_state.current_user))
            c.execute("DELETE FROM requests WHERE sender=? AND receiver=?", (req, st.session_state.current_user))
            conn.commit()
            st.experimental_rerun()

    # Send request
    st.markdown("**Send Friend Request:**")
    all_users = [u[0] for u in c.execute("SELECT username FROM users").fetchall()]
    potential = [u for u in all_users if u != st.session_state.current_user and u not in friends and u not in requests]
    new_friend = st.selectbox("Select user", [""] + potential)
    if st.button("Send Request") and new_friend:
        c.execute("INSERT INTO requests VALUES (?,?)", (st.session_state.current_user, new_friend))
        conn.commit()
        st.success(f"Friend request sent to {new_friend}")

# -------------------- NOTIFICATIONS --------------------
elif st.session_state.page == "notifications":
    nav_buttons()
    st.subheader("🔔 Notifications")
    c.execute("SELECT content, timestamp FROM notifications WHERE user=? ORDER BY timestamp DESC", (st.session_state.current_user,))
    notifications = c.fetchall()
    for n in notifications:
        st.write(f"{n[1]} - {n[0]}")
    if st.button("Clear Notifications"):
        c.execute("DELETE FROM notifications WHERE user=?", (st.session_state.current_user,))
        conn.commit()
        st.experimental_rerun()

/* ===============================
   Zeta Chat - Dark Mode Modern Theme
   =============================== */

body {
    background-color: #1c1f26;
    color: #e0e0e0;
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}

/* Headers */
h1, h2, h3, h4 {
    color: #ffffff;
    font-weight: 700;
}

/* Sidebar */
.stSidebar {
    background-color: #22252d !important;
    color: #e0e0e0 !important;
    border-right: 2px solid #2f3136;
    padding: 1rem;
}

/* Buttons */
div.stButton > button {
    background-color: #5a6cff;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.6rem 1.5rem;
    font-weight: 600;
    transition: all 0.2s ease-in-out;
}
div.stButton > button:hover {
    background-color: #4048c0;
    transform: scale(1.05);
}

/* Inputs */
.stTextInput > div > div > input, .stTextArea textarea {
    background-color: #2a2d36;
    color: #ffffff;
    border: 1px solid #444753;
    border-radius: 8px;
    padding: 0.5rem;
}
.stTextInput > div > div > input:focus, .stTextArea textarea:focus {
    border: 1px solid #5a6cff;
    outline: none;
}

/* Navigation */
.nav-bar {
    display: flex;
    justify-content: space-around;
    background-color: #1f222b;
    padding: 0.5rem;
    border-bottom: 2px solid #2f3136;
    margin-bottom: 1rem;
}
.nav-bar button {
    background-color: transparent;
    border: none;
    color: #e0e0e0;
    font-weight: 600;
    padding: 0.5rem 1rem;
    transition: color 0.2s ease-in-out;
    cursor: pointer;
}
.nav-bar button:hover {
    color: #5a6cff;
    transform: scale(1.05);
}

/* Feed Cards */
.feed-card {
    background-color: #2a2d36;
    border-radius: 12px;
    padding: 1rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    margin-bottom: 1.5rem;
    transition: transform 0.15s ease;
}
.feed-card:hover {
    transform: translateY(-2px) scale(1.01);
}

/* Comments */
.comment-reply {
    background-color: #1f222b;
    color: #c0c0c0;
    border-left: 3px solid #5a6cff;
    padding: 0.4rem 0.8rem;
    margin: 0.3rem 0;
    border-radius: 6px;
}

/* Chat bubbles */
.chat-bubble {
    padding: 0.5rem 1rem;
    border-radius: 12px;
    margin: 0.3rem 0;
    max-width: 70%;
}
.chat-bubble.user {
    background-color: #5a6cff;
    color: #ffffff;
    align-self: flex-end;
}
.chat-bubble.friend {
    background-color: #3b3f4c;
    color: #ffffff;
    align-self: flex-start;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 10px;
}
::-webkit-scrollbar-thumb {
    background-color: #5a6cff;
    border-radius: 10px;
}
::-webkit-scrollbar-track {
    background: #1c1f26;
}

/* Friend Requests */
.friend-request-card {
    background-color: #2a2d36;
    border-radius: 10px;
    padding: 0.6rem;
    margin-bottom: 0.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* Notifications */
.notification-card {
    background-color: #2a2d36;
    border-radius: 8px;
    padding: 0.6rem;
    margin-bottom: 0.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}
