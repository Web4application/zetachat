import streamlit as st
import sqlite3
import time
from random import randint, choice

# ======================
# 🎨 Modern Dark Theme CSS
# ======================
dark_style = """
body { background-color:#121212; color:#e0e0e0; font-family:'Segoe UI',Roboto,sans-serif; }
.stApp { background-color:#121212; }
.stSidebar { background-color:#1f1f1f !important; }
div.stButton>button { background-color:#4e5bdc; color:white; border-radius:6px; padding:0.5rem 1rem; }
div.stButton>button:hover { background-color:#3a43a5; }
.stTextInput>div>div>input, .stTextArea textarea { background-color:#1f1f1f; color:#e0e0e0; border-radius:6px; }
.feed-card { background-color:#1f1f1f; border-radius:10px; padding:1rem; margin-bottom:1.5rem; }
.comment-reply { background-color:#2a2a2a; border-left:3px solid #4e5bdc; padding:0.4rem 0.8rem; margin:0.3rem 0; border-radius:4px; }
.comment-reply-2 { background-color:#333; border-left:3px solid #00ccff; margin-left:20px; padding:0.3rem 0.6rem; border-radius:4px; }
.chat-bubble { background-color:#2a2a2a; padding:0.5rem; border-radius:12px; margin:3px 0; max-width:60%; }
.chat-bubble.sender { background-color:#4e5bdc; color:white; margin-left:auto; }
"""
st.markdown(f"<style>{dark_style}</style>", unsafe_allow_html=True)

# ======================
# 🧠 SQLite Database
# ======================
conn = sqlite3.connect("zetachat.db", check_same_thread=False)
c = conn.cursor()
# Users
c.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT, avatar TEXT, bio TEXT)""")
# Posts
c.execute("""CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT, content TEXT, image TEXT, likes INTEGER, time TEXT)""")
# Comments
c.execute("""CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY AUTOINCREMENT, post_id INTEGER, user TEXT, content TEXT, parent INTEGER)""")
# Messages
c.execute("""CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, sender TEXT, receiver TEXT, message TEXT, time TEXT)""")
# Friends
c.execute("""CREATE TABLE IF NOT EXISTS friends (id INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT, friend TEXT)""")
# Friend Requests
c.execute("""CREATE TABLE IF NOT EXISTS friend_requests (id INTEGER PRIMARY KEY AUTOINCREMENT, sender TEXT, receiver TEXT)""")
# Notifications
c.execute("""CREATE TABLE IF NOT EXISTS notifications (id INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT, message TEXT, time TEXT)""")
conn.commit()

# ======================
# 🔐 Session State
# ======================
if "current_user" not in st.session_state: st.session_state.current_user=None

# ======================
# 🛠 Helper Functions
# ======================
def get_user(username):
    c.execute("SELECT username, avatar, bio FROM users WHERE username=?", (username,))
    r = c.fetchone()
    return {"username": r[0], "avatar": r[1], "bio": r[2]} if r else {}

def login_user(username, password):
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    r = c.fetchone()
    return r and r[0]==password

def signup_user(username, password):
    c.execute("SELECT username FROM users WHERE username=?", (username,))
    if c.fetchone(): return False
    avatar = f"https://i.pravatar.cc/50?img={randint(1,70)}"
    c.execute("INSERT INTO users (username,password,avatar,bio) VALUES (?,?,?,?)",(username,password,avatar,"New user bio"))
    conn.commit()
    return True

def create_post(user, content, image=""):
    c.execute("INSERT INTO posts (user, content, image, likes, time) VALUES (?,?,?,?,?)",(user, content, image, 0, time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

def get_posts():
    c.execute("SELECT id,user, content, image, likes, time FROM posts ORDER BY id DESC")
    posts = []
    for r in c.fetchall():
        c.execute("SELECT user,content,parent FROM comments WHERE post_id=?",(r[0],))
        comments = [{"user":cm[0],"content":cm[1],"parent":cm[2]} for cm in c.fetchall()]
        posts.append({"id":r[0],"user":r[1],"content":r[2],"image":r[3],"likes":r[4],"time":r[5],"comments":comments})
    return posts

def add_comment(post_id,user,content,parent=None):
    c.execute("INSERT INTO comments (post_id,user,content,parent) VALUES (?,?,?,?)",(post_id,user,content,parent))
    conn.commit()

def like_post(post_id):
    c.execute("UPDATE posts SET likes = likes + 1 WHERE id=?",(post_id,))
    conn.commit()

def send_message(sender, receiver, message):
    c.execute("INSERT INTO messages (sender, receiver, message, time) VALUES (?,?,?,?)",(sender, receiver, message, time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

def get_messages(u1,u2):
    c.execute("""SELECT sender,message,time FROM messages WHERE (sender=? AND receiver=?) OR (sender=? AND receiver=?) ORDER BY id ASC""",(u1,u2,u2,u1))
    return [{"sender":r[0],"message":r[1],"time":r[2]} for r in c.fetchall()]

def add_notification(user, message):
    c.execute("INSERT INTO notifications (user,message,time) VALUES (?,?,?)",(user,message,time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

def get_notifications(user):
    c.execute("SELECT message FROM notifications WHERE user=? ORDER BY id DESC",(user,))
    return [r[0] for r in c.fetchall()]

def add_friend(user, friend):
    c.execute("INSERT INTO friends (user, friend) VALUES (?,?)",(user, friend))
    conn.commit()

def get_friends(user):
    c.execute("SELECT friend FROM friends WHERE user=?",(user,))
    return [r[0] for r in c.fetchall()]

def send_friend_request(sender, receiver):
    c.execute("INSERT INTO friend_requests (sender, receiver) VALUES (?,?)",(sender, receiver))
    conn.commit()

def get_friend_requests(user):
    c.execute("SELECT sender FROM friend_requests WHERE receiver=?",(user,))
    return [r[0] for r in c.fetchall()]

def accept_friend_request(sender, receiver):
    add_friend(sender, receiver)
    add_friend(receiver, sender)
    c.execute("DELETE FROM friend_requests WHERE sender=? AND receiver=?",(sender, receiver))
    conn.commit()

# ======================
# 🌐 App Layout
# ======================
st.set_page_config(page_title="Zeta Chat", layout="wide")
pages = ["Login","Feed","Chat","Friends","Notifications","Profile"]
page_choice = st.sidebar.radio("Navigation", pages)

# ======================
# ---------- Login Page ----------
# ======================
if page_choice=="Login":
    st.title("Zeta Chat")
    st.subheader("Login")
    login_user_input = st.text_input("Username")
    login_pass_input = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(login_user_input, login_pass_input):
            st.session_state.current_user = login_user_input
            st.success("Logged in! Go to Feed.")
        else: st.error("Invalid credentials")

    st.subheader("Signup")
    signup_user_input = st.text_input("New Username")
    signup_pass_input = st.text_input("New Password", type="password")
    if st.button("Signup"):
        if signup_user(signup_user_input, signup_pass_input):
            st.success("Account created! Please login.")
        else: st.error("Username exists!")

# ======================
# ---------- Feed Page ----------
# ======================
elif page_choice=="Feed" and st.session_state.current_user:
    st.header("Feed")
    user = get_user(st.session_state.current_user)
    post_content = st.text_area("What's on your mind?")
    post_image = st.text_input("Image URL (optional)")
    if st.button("Post"):
        if post_content.strip()!="":
            create_post(user["username"], post_content, post_image)
            add_notification(user["username"], "You posted a new status!")
            st.experimental_rerun()

    for post in get_posts():
        st.markdown(f"<div class='feed-card'>", unsafe_allow_html=True)
        st.write(f"**{post['user']}** • {post['time']}")
        st.write(post["content"])
        if post["image"]: st.image(post["image"])
        col1,col2 = st.columns([1,2])
        with col1:
            if st.button(f"👍 Like {post['id']}"):
                like_post(post['id'])
                add_notification(post['user'], f"{st.session_state.current_user} liked your post")
                st.experimental_rerun()
        with col2:
            comment_input = st.text_input(f"💬 Comment {post['id']}", key=f"comment_{post['id']}")
            if st.button(f"Comment {post['id']}") and comment_input.strip():
                add_comment(post['id'], st.session_state.current_user, comment_input)
                add_notification(post['user'], f"{st.session_state.current_user} commented on your post")
                st.experimental_rerun()

        # Show threaded comments
        for cm in post['comments']:
            style = "comment-reply-2" if cm['parent'] else "comment-reply"
            st.markdown(f"<div class='{style}'>{cm['user']}: {cm['content']}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("---")
        time.sleep(0.05)

# ======================
# ---------- Chat Page ----------
# ======================
elif page_choice=="Chat" and st.session_state.current_user:
    st.header("Chat")
    users = [r[0] for r in c.execute("SELECT username FROM users").fetchall() if r[0]!=st.session_state.current_user]
    chat_user = st.selectbox("Select user to chat", users)
    message = st.text_input("Message")
    if st.button("Send"):
        if message.strip():
            send_message(st.session_state.current_user, chat_user, message)
            add_notification(chat_user, f"New message from {st.session_state.current_user}")
            st.experimental_rerun()
    st.subheader("Messages")
    for m in get_messages(st.session_state.current_user, chat_user):
        cls = "chat-bubble sender" if m["sender"]==st.session_state.current_user else "chat-bubble"
        st.markdown(f"<div class='{cls}'>{m['sender']}: {m['message']}</div>", unsafe_allow_html=True)
