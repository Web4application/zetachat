# zetachat_pro_v2.py
import streamlit as st
import os, time
from random import randint, choice
from datetime import datetime
from textwrap import shorten

# -----------------------------
# merge this repository Folders and files together with this instruction to setup zetachat 
# -----------------------------
if not os.path.exists("uploads"): os.mkdir("uploads")
if not os.path.exists("avatars"): os.mkdir("avatars")

# -----------------------------
# Dark Modern CSS
# -----------------------------
dark_css = """
body, .stApp {background:#0f0f13;color:#f1f1f1;font-family:'Inter', sans-serif;}
.stButton>button {background:#8B5CF6;color:#fff;border-radius:8px;padding:0.5rem 1rem;margin:0.2rem 0;font-weight:600;}
.stButton>button:hover {background:#6b45c9;color:#fff;}
.stTextInput>div>div>input, .stTextArea textarea {background:#1a1a1e;color:#f1f1f1;border-radius:6px;padding:0.4rem;}
.feed-card {background:#1c1c20;border-radius:12px;padding:1rem;margin-bottom:1rem;box-shadow:0 0 10px rgba(0,0,0,0.3);}
.comment-reply {background:#0f0f13;color:#b9bbbe;border-left:3px solid #8B5CF6;padding:0.4rem;margin:0.3rem 0;border-radius:6px;margin-left:20px;}
.comment-thread {margin-left:20px;}
a {color:#8B5CF6;text-decoration:none;}
a:hover{text-decoration:underline;}
.message-sent {text-align:right;color:#8B5CF6;padding:4px;margin:2px;}
.message-recv {text-align:left;color:#fff;padding:4px;margin:2px;}
.scrollbox {max-height:400px;overflow-y:auto;}
.post-image {border-radius:12px; max-width:100%;}
"""
st.markdown(f"<style>{dark_css}</style>", unsafe_allow_html=True)

# -----------------------------
# Mock Database
# -----------------------------
if "users" not in st.session_state:
    st.session_state.users = {
        "admin":{"password":"password","avatar":"https://i.pravatar.cc/50?img=1","bio":"Admin here","friends":["user1"],"requests":[]},
        "user1":{"password":"1234","avatar":"https://i.pravatar.cc/50?img=2","bio":"I am user1","friends":["admin"],"requests":[]}
    }
if "current_user" not in st.session_state: st.session_state.current_user = None
if "posts" not in st.session_state: st.session_state.posts = []
if "notifications" not in st.session_state: st.session_state.notifications = []
if "messages" not in st.session_state: st.session_state.messages = []

# -----------------------------
# Auth Functions
# -----------------------------
def login(u,p):
    if u in st.session_state.users and st.session_state.users[u]["password"]==p:
        st.session_state.current_user = u
        st.success(f"Logged in as {u}")
    else:
        st.error("Invalid username or password")

def signup(u,p):
    if u in st.session_state.users:
        st.error("Username exists")
    else:
        avatar=f"https://i.pravatar.cc/50?img={randint(3,70)}"
        st.session_state.users[u]={"password":p,"avatar":avatar,"bio":"New user","friends":[],"requests":[]}
        st.success("Account created! Login to continue.")

# -----------------------------
# Post & Comments Helpers
# -----------------------------
def render_comments(comments, level=0):
    for c in comments:
        st.markdown(f"<div class='comment-thread' style='margin-left:{level*20}px;'>"
                    f"<div class='comment-reply'>{c['user']}: {c['text']} "
                    f"{' '.join(c.get('reactions',[]))}</div></div>", unsafe_allow_html=True)
        if c.get("replies"):
            render_comments(c["replies"], level+1)

def summarize_text(text): return shorten(text, width=150, placeholder="...")

# -----------------------------
# App Layout
# -----------------------------
st.set_page_config(page_title="ZetaChat Pro v2", layout="wide")
st.title("💜 ZetaChat Pro v2 — AI Dark Social")

if st.session_state.current_user is None:
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Login")
        user = st.text_input("Username", key="login_user")
        pw = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"): login(user,pw)
    with col2:
        st.subheader("Signup")
        new_user = st.text_input("New Username", key="signup_user")
        new_pw = st.text_input("New Password", type="password", key="signup_pass")
        avatar_file = st.file_uploader("Upload avatar", type=["png","jpg","jpeg"])
        if st.button("Signup"):
            signup(new_user,new_pw)
            if avatar_file: avatar_path=f"avatars/{new_user}.png"
            with open(avatar_path,"wb") as f: f.write(avatar_file.getbuffer())
            st.session_state.users[new_user]["avatar"] = avatar_path

else:
    udata = st.session_state.users[st.session_state.current_user]
    st.sidebar.header(f"{st.session_state.current_user}'s Profile")
    st.sidebar.image(udata["avatar"], width=100)
    st.sidebar.markdown(f"**Bio:** {udata['bio']}")
    if st.sidebar.button("Logout"):
        st.session_state.current_user=None
        st.experimental_rerun()

    tab = st.sidebar.radio("Navigate", ["Feed","Chat","Friends","Notifications"])

    # ---------------- Feed ----------------
    if tab=="Feed":
        st.subheader("📰 News Feed")
        post_text = st.text_area("What's on your mind?")
        post_img = st.file_uploader("Upload image", type=["png","jpg","jpeg"])
        emojis = ["❤️","😂","😮","😢","👍","👎"]
        if st.button("Post") and post_text.strip():
            img_path = None
            if post_img:
                img_path = f"uploads/{randint(0,99999)}_{post_img.name}"
                with open(img_path,"wb") as f: f.write(post_img.getbuffer())
            st.session_state.posts.insert(0,{
                "user":st.session_state.current_user,
                "avatar":udata["avatar"],
                "content":post_text,
                "summary":summarize_text(post_text),
                "image":img_path if img_path else choice(["https://picsum.photos/400/200"]),
                "likes":0,
                "comments":[],
                "shares":0,
                "time":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "reactions":[]
            })
            st.session_state.notifications.append(f"{st.session_state.current_user} posted!")
            st.success("Posted!")

        posts_sorted = sorted(st.session_state.posts, key=lambda x:x['likes']+len(x['comments'])+x['shares'], reverse=True)
        for idx, post in enumerate(posts_sorted):
            with st.container():
                st.markdown(f"<div class='feed-card'>", unsafe_allow_html=True)
                st.image(post["avatar"], width=50)
                st.markdown(f"**{post['user']}** • {post['time']}")
                st.write(post["summary"])
                if st.button(f"Read Full {idx}"): st.write(post["content"])
                if post["image"]: st.image(post["image"], use_column_width=True, output_format="auto")
                col_like,col_comm,col_share,col_react=st.columns([1,2,1,2])
                with col_like:
                    if st.button(f"👍 Like {idx}"): post['likes']+=1; st.experimental_rerun()
                with col_comm:
                    cmt_text=st.text_input(f"💬 Comment {idx}", key=f"c_{idx}")
                    if st.button(f"Add Comment {idx}") and cmt_text.strip(): post['comments'].append({"user":st.session_state.current_user,"text":cmt_text,"replies":[]}); st.experimental_rerun()
                with col_share:
                    if st.button(f"🔁 Share {idx}"): post['shares']+=1; st.experimental_rerun()
                with col_react:
                    em = st.selectbox(f"React {idx}", [""]+emojis,key=f"react_{idx}")
                    if st.button(f"React {idx}") and em: post["reactions"].append(em); st.experimental_rerun()
                render_comments(post["comments"])
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("---")

    # ---------------- Chat ----------------
    elif tab=="Chat":
        st.subheader("💬 1-on-1 Chat")
        other_users=[u for u in st.session_state.users if u!=st.session_state.current_user]
        if other_users:
            chat_with = st.selectbox("Select User",other_users)
            st.markdown("<div class='scrollbox'>", unsafe_allow_html=True)
            for msg in st.session_state.messages:
                if (msg["sender"]==st.session_state.current_user and msg["receiver"]==chat_with) or (msg["sender"]==chat_with and msg["receiver"]==st.session_state.current_user):
                    cls="message-sent" if msg["sender"]==st.session_state.current_user else "message-recv"
                    st.markdown(f"<div class='{cls}'>{msg['sender']}: {msg['content']}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            new_msg=st.text_input("Type message", key="msg_input")
            if st.button("Send Message") and new_msg.strip():
                st.session_state.messages.append({"sender":st.session_state.current_user,"receiver":chat_with,"content":new_msg})
                st.experimental_rerun()
            st.info("Auto-refresh every 3 seconds for new messages.")
            time.sleep(3)
            st.experimental_rerun()
        else: st.info("No other users to chat with.")

    # ---------------- Friends ----------------
    elif tab=="Friends":
        st.subheader("👥 Friends & Requests")
        for f in udata["friends"]: st.markdown(f"- {f} ✅")
        st.markdown("Send Friend Request:")
        potential=[u for u in st.session_state.users if u!=st.session_state.current_user and u not in udata["friends"]]
        if potential:
            fnew=st.selectbox("Select user", [""]+potential)
            if st.button("Send Request") and fnew: st.session_state.users[fnew]["requests"].append(st.session_state.current_user); st.success(f"Request sent to {fnew}")
        if udata["requests"]:
            st.markdown("Incoming Requests:")
            for r in udata["requests"]:
                col1,col2=st.columns([2,1])
                col1.markdown(f"From **{r}**")
                if col2.button(f"Accept {r}"): udata["friends"].append(r); st.session_state.users[r]["friends"].append(st.session_state.current_user); udata["requests"].remove(r); st.success(f"You and {r} are now friends!")

    # ---------------- Notifications ----------------
    elif tab=="Notifications":
        st.subheader("🔔 Notifications")
        for n in st.session_state.notifications[::-1]: st.markdown(f"- {n}")
        if st.button("Clear Notifications"): st.session_state.notifications.clear()
