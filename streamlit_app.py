# zeta_all_in_one.py
import streamlit as st
import sqlite3
import os
from datetime import datetime
from random import randint
import time

# ------------------------------
# Auto-create uploads folder
# ------------------------------
if not os.path.exists("uploads"):
    os.mkdir("uploads")

# ------------------------------
# SQLite DB (local, single file)
# ------------------------------
conn = sqlite3.connect("zeta.db", check_same_thread=False)
c = conn.cursor()

# Users
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    avatar TEXT,
    bio TEXT
)
""")
# Posts
c.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    content TEXT,
    image TEXT,
    likes INTEGER DEFAULT 0,
    created_at TEXT
)
""")
# Messages
c.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT,
    receiver TEXT,
    content TEXT,
    created_at TEXT
)
""")
# Friends
c.execute("""
CREATE TABLE IF NOT EXISTS friends (
    user TEXT,
    friend TEXT,
    status TEXT
)
""")
# Comments
c.execute("""
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER,
    user TEXT,
    content TEXT,
    created_at TEXT
)
""")
conn.commit()

# ------------------------------
# Dark modern CSS
# ------------------------------
dark_css = """
body, .stApp {background-color:#0d0d0f;color:#eaeaea;font-family:'Inter', sans-serif;}
button,input,textarea {background:#1e1e22;color:#fff;border-radius:8px;}
.feed-card {background-color:#1b1b1f;border-radius:10px;padding:1rem;margin-bottom:1rem;box-shadow:0 0 5px rgba(255,255,255,0.05);}
.comment-reply {background-color:#0d0d12;color:#b9bbbe;border-left:3px solid #8B5CF6;padding:0.4rem 0.8rem;margin:0.3rem 0;border-radius:4px;}
.glow-avatar {border-radius:50%;border:3px solid #8B5CF6;padding:2px;}
"""
st.markdown(f"<style>{dark_css}</style>", unsafe_allow_html=True)

# ------------------------------
# Session state
# ------------------------------
if "current_user" not in st.session_state: st.session_state.current_user = None
if "notifications" not in st.session_state: st.session_state.notifications = []

# ------------------------------
# Auth functions
# ------------------------------
def login(username, password):
    user = c.execute("SELECT * FROM users WHERE username=? AND password=?", (username,password)).fetchone()
    if user:
        st.session_state.current_user = username
        st.success(f"Logged in as {username}")
    else:
        st.error("Invalid username or password")

def signup(username, password):
    exists = c.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
    if exists:
        st.error("Username already exists")
    else:
        avatar = f"https://i.pravatar.cc/50?img={randint(1,70)}"
        c.execute("INSERT INTO users (username,password,avatar,bio) VALUES (?,?,?,?)",
                  (username,password,avatar,"Hello! I am new here."))
        conn.commit()
        st.success("Account created! Please log in.")

# ------------------------------
# App Layout
# ------------------------------
st.set_page_config(page_title="Zeta App", layout="wide")
st.title("💫 Zeta — Full Social Dark Mode (All-in-One)")

# Auto-refresh for real-time
st_autorefresh = st.experimental_rerun
if st.button("Refresh Now"):
    st.experimental_rerun()

# ---------- LOGIN/SIGNUP ----------
if st.session_state.current_user is None:
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Login")
        login_user = st.text_input("Username", key="login_user")
        login_pass = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            login(login_user, login_pass)
    with col2:
        st.subheader("Signup")
        signup_user = st.text_input("New Username", key="signup_user")
        signup_pass = st.text_input("New Password", type="password", key="signup_pass")
        if st.button("Signup"):
            signup(signup_user, signup_pass)

else:
    user_data = c.execute("SELECT * FROM users WHERE username=?", (st.session_state.current_user,)).fetchone()
    st.sidebar.header(f"{st.session_state.current_user}'s Profile")
    st.sidebar.image(user_data[2], width=100)
    st.sidebar.markdown(f"**Bio:** {user_data[3]}")
    if st.sidebar.button("Logout"):
        st.session_state.current_user = None
        st.experimental_rerun()

    # Tabs
    tab = st.sidebar.radio("Navigate", ["Feed","Chat","Friends","Profile","Notifications"])

    # ------------------- FEED -------------------
    if tab=="Feed":
        st.subheader("📣 Create a Post")
        post_text = st.text_area("What's on your mind?")
        post_image = st.file_uploader("Upload Image (optional)", type=["png","jpg","jpeg"])
        if st.button("Post"):
            image_path = ""
            if post_image:
                image_path = f"uploads/{post_image.name}"
                with open(image_path,"wb") as f: f.write(post_image.getbuffer())
            c.execute("INSERT INTO posts (user,content,image,created_at) VALUES (?,?,?,?)",
                      (st.session_state.current_user,post_text,image_path,datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()
            st.success("Posted!")
            st.experimental_rerun()

        st.subheader("📰 News Feed")
        posts = c.execute("SELECT * FROM posts ORDER BY id DESC").fetchall()
        for p in posts:
            st.markdown("<div class='feed-card'>", unsafe_allow_html=True)
            st.markdown(f"**{p[1]}**  •  {p[5]}")
            st.write(p[2])
            if p[3]: st.image(p[3])

            # Likes
            col_like,col_comment = st.columns([1,3])
            with col_like:
                if st.button(f"👍 Like {p[0]}"):
                    c.execute("UPDATE posts SET likes=likes+1 WHERE id=?", (p[0],))
                    conn.commit()
                    st.session_state.notifications.append(f"{st.session_state.current_user} liked {p[1]}'s post")
                    st.experimental_rerun()
                st.markdown(f"Likes: {p[4]}")

            # Comments
            with col_comment:
                comments = c.execute("SELECT * FROM comments WHERE post_id=? ORDER BY id ASC", (p[0],)).fetchall()
                for cm in comments:
                    st.markdown(f"<div class='comment-reply'><b>{cm[2]}</b>: {cm[3]}</div>", unsafe_allow_html=True)
                comment_text = st.text_input(f"💬 Comment {p[0]}", key=f"comment_{p[0]}")
                if st.button(f"Comment {p[0]}") and comment_text.strip():
                    c.execute("INSERT INTO comments (post_id,user,content,created_at) VALUES (?,?,?,?)",
                              (p[0], st.session_state.current_user, comment_text, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    conn.commit()
                    st.session_state.notifications.append(f"{st.session_state.current_user} commented on {p[1]}'s post")
                    st.experimental_rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    # ------------------- CHAT -------------------
    elif tab=="Chat":
        st.subheader("💬 Direct Messages")
        users = c.execute("SELECT username FROM users WHERE username!=?", (st.session_state.current_user,)).fetchall()
        chat_user = st.selectbox("Select user", [""] + [u[0] for u in users])
        if chat_user:
            msgs = c.execute("SELECT * FROM messages WHERE (sender=? AND receiver=?) OR (sender=? AND receiver=?) ORDER BY id ASC",
                             (st.session_state.current_user,chat_user,chat_user,st.session_state.current_user)).fetchall()
            for m in msgs:
                st.markdown(f"**{m[1]} → {m[2]}:** {m[3]}")
            msg_text = st.text_input("Type message")
            if st.button("Send Message"):
                c.execute("INSERT INTO messages (sender,receiver,content,created_at) VALUES (?,?,?,?)",
                          (st.session_state.current_user,chat_user,msg_text,datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                conn.commit()
                st.experimental_rerun()

    # ------------------- FRIENDS -------------------
    elif tab=="Friends":
        st.subheader("💜 Friends System")
        all_users = c.execute("SELECT username FROM users WHERE username!=?", (st.session_state.current_user,)).fetchall()
        all_users = [u[0] for u in all_users]
        st.markdown("**Friend Requests:**")
        requests = c.execute("SELECT user FROM friends WHERE friend=? AND status='request'", (st.session_state.current_user,)).fetchall()
        for r in requests:
            col1,col2 = st.columns([2,1])
            col1.markdown(f"{r[0]} wants to be your friend")
            with col2:
                if st.button(f"Accept {r[0]}"):
                    c.execute("UPDATE friends SET status='accepted' WHERE user=? AND friend=?", (r[0],st.session_state.current_user))
                    c.execute("INSERT INTO friends (user,friend,status) VALUES (?,?,?)", (st.session_state.current_user,r[0],'accepted'))
                    conn.commit()
                    st.session_state.notifications.append(f"You are now friends with {r[0]}")
                    st.experimental_rerun()
                if st.button(f"Reject {r[0]}"):
                    c.execute("DELETE FROM friends WHERE user=? AND friend=?", (r[0],st.session_state.current_user))
                    conn.commit()
                    st.experimental_rerun()

        st.markdown("**Add Friends:**")
        for u in all_users:
            status = c.execute("SELECT * FROM friends WHERE user=? AND friend=?", (st.session_state.current_user,u)).fetchone()
            if not status:
                if st.button(f"Add {u}"):
                    c.execute("INSERT INTO friends (user,friend,status) VALUES (?,?,?)",(st.session_state.current_user,u,'pending'))
                    c.execute("INSERT INTO friends (user,friend,status) VALUES (?,?,?)",(u,st.session_state.current_user,'request'))
                    conn.commit()
                    st.session_state.notifications.append(f"Friend request sent to {u}")
                    st.experimental_rerun()

        st.markdown("**Your Friends:**")
        friends = c.execute("SELECT friend FROM friends WHERE user=? AND status='accepted'", (st.session_state.current_user,)).fetchall()
        st.write([f[0] for f in friends])

    # ------------------- PROFILE -------------------
    elif tab=="Profile":
        st.subheader("👤 Profile")
        st.text_input("Username", value=user_data[0], disabled=True)
        bio_text = st.text_area("Bio", value=user_data[3])
        if st.button("Update Bio"):
            c.execute("UPDATE users SET bio=? WHERE username=?", (bio_text, st.session_state.current_user))
            conn.commit()
            st.success("Bio updated!")

    # ------------------- NOTIFICATIONS -------------------
    elif tab=="Notifications":
        st.subheader("🔔 Notifications")
        for n in st.session_state.notifications[::-1]:
            st.markdown(f"- {n}")
        if st.button("Clear Notifications"):
            st.session_state.notifications.clear()
