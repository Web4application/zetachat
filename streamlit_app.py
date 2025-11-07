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
