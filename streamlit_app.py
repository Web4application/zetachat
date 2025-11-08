import streamlit as st
import time
from random import choice, randint
import os

# ==============================
# 🎨 Dark Theme CSS
# ==============================
dark_css = """
body {background-color: #121212; color: #e0e0e0; font-family: 'Segoe UI', Roboto, sans-serif;}
.stApp {background-color: #121212;}
h1,h2,h3,h4,h5,h6{color:#fff;}
.stSidebar {background-color:#1f1f1f; color:#e0e0e0;}
div.stButton > button {background-color:#0078d4; color:white; border-radius:6px;}
div.stButton > button:hover {background-color:#005a9e; color:white;}
.stTextInput>div>div>input, .stTextArea textarea {background-color:#1f1f1f; color:#e0e0e0; border-radius:6px;}
.feed-card {background-color:#1f1f1f; border-radius:10px; padding:1rem; margin-bottom:1rem;}
.comment-reply {background-color:#2a2a2a; color:#cfcfcf; border-left:3px solid #0078d4; padding:0.4rem 0.8rem; margin:0.3rem 0; border-radius:4px;}
"""

st.markdown(f"<style>{dark_css}</style>", unsafe_allow_html=True)

# ==============================
# 🧠 Mock Database each session should land on dofferent page
# ==============================
if "users" not in st.session_state:
    st.session_state.users = {
        "admin": {"password":"password", "avatar":"https://i.pravatar.cc/50?img=1","bio":"Hello! I'm admin.","friends":["user1"],"requests":[]},
        "user1": {"password":"1234","avatar":"https://i.pravatar.cc/50?img=2","bio":"I am user1.","friends":["admin"],"requests":[]}
    }

if "current_user" not in st.session_state:
    st.session_state.current_user = None

if "posts" not in st.session_state:
    st.session_state.posts = []

if "notifications" not in st.session_state:
    st.session_state.notifications = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = {}

sample_images = [f"https://picsum.photos/400/200?random={i}" for i in range(1,5)]

# ==============================
# 🔐 Auth Functions
# ==============================
def login(username,password):
    if username in st.session_state.users and st.session_state.users[username]["password"]==password:
        st.session_state.current_user=username
        st.success(f"Logged in as {username}")
    else:
        st.error("Invalid username or password")

def signup(username,password):
    if username in st.session_state.users:
        st.error("Username already exists")
    else:
        avatar_url=f"https://i.pravatar.cc/50?img={randint(5,70)}"
        st.session_state.users[username]={"password":password,"avatar":avatar_url,"bio":"New user bio","friends":[],"requests":[]}
        st.success("Account created! Please log in.")

def reset_password(username,new_password):
    if username in st.session_state.users:
        st.session_state.users[username]["password"] = new_password
        st.success("Password reset successfully!")
    else:
        st.error("Username does not exist")

# ==============================
# 🌐 Pages
# ==============================
if st.session_state.current_user:
    page = st.sidebar.radio("Navigate", ["Feed","Chat","Profile"])
else:
    page = "Login / Signup"

# ----------------------
# Login / Signup / Forgot Password Page
# ----------------------
if page=="Login / Signup":
    st.title("🔹 ZetaChat Login")
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Login")
        login_user = st.text_input("Username", key="login_user")
        login_pass = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            login(login_user, login_pass)

        st.markdown("**Forgot Password?**")
        forgot_user = st.text_input("Enter Username to reset", key="forgot_user")
        new_pass = st.text_input("New Password", type="password", key="new_pass")
        if st.button("Reset Password"):
            reset_password(forgot_user, new_pass)

    with col2:
        st.subheader("Signup")
        signup_user = st.text_input("New Username", key="signup_user")
        signup_pass = st.text_input("New Password", type="password", key="signup_pass")
        if st.button("Signup"):
            signup(signup_user, signup_pass)

# ----------------------
# Feed Page
# ----------------------
elif page=="Feed" and st.session_state.current_user:
    user = st.session_state.users[st.session_state.current_user]

    st.sidebar.header(f"{st.session_state.current_user}'s Profile")
    st.sidebar.image(user["avatar"])
    st.sidebar.markdown(f"**Bio:** {user['bio']}")
    if st.sidebar.button("Logout"):
        st.session_state.current_user=None
        st.experimental_rerun()

    st.sidebar.subheader("Notifications")
    for n in st.session_state.notifications[::-1]:
        st.sidebar.markdown(f"- {n}")
    st.sidebar.button("Clear Notifications", on_click=lambda: st.session_state.notifications.clear())

    st.sidebar.subheader("Friends")
    for f in user["friends"]:
        if st.sidebar.button(f"View {f}'s Profile"):
            st.session_state.view_profile=f
            st.experimental_rerun()

    # View Feed
    st.subheader("📣 Create a Post")
    post_text=st.text_area("What's on your mind?")
    post_image_url=st.text_input("Image URL (optional)","")
    if st.button("Post"):
        if post_text.strip()!="":
            post={"user":st.session_state.current_user,"avatar":user["avatar"],"content":post_text,"image":post_image_url if post_image_url else choice(sample_images),"likes":0,"comments":[],"shares":0,"time":time.strftime("%Y-%m-%d %H:%M:%S")}
            st.session_state.posts.insert(0,post)
            st.session_state.notifications.append(f"{st.session_state.current_user} posted a new status!")
            st.success("Posted!")

    st.subheader("📰 News Feed")
    for idx, post in enumerate(st.session_state.posts):
        if post["user"]!=st.session_state.current_user and post["user"] not in user["friends"]:
            continue
        with st.container():
            st.markdown(f"<div class='feed-card'>",unsafe_allow_html=True)
            col1,col2=st.columns([1,5])
            with col1: st.image(post["avatar"], width=50)
            with col2:
                st.markdown(f"**{post['user']}** • {post['time']}")
                st.write(post["content"])
                if post["image"]: st.image(post["image"])
            col_like,col_comment,col_share=st.columns([1,2,1])
            with col_like:
                if st.button(f"👍 Like {idx}"):
                    st.session_state.posts[idx]['likes']+=1
                    st.session_state.notifications.append(f"{st.session_state.current_user} liked {post['user']}'s post!")
            with col_comment:
                comment_input=st.text_input(f"💬 Comment {idx}", key=f"comment_{idx}")
                if st.button(f"Add Comment {idx}") and comment_input.strip():
                    st.session_state.posts[idx]['comments'].append(f"{st.session_state.current_user}: {comment_input}")
                    st.session_state.notifications.append(f"{st.session_state.current_user} commented on {post['user']}'s post!")
            with col_share:
                if st.button(f"🔁 Share {idx}"):
                    st.session_state.posts[idx]['shares']+=1
                    st.session_state.notifications.append(f"{st.session_state.current_user} shared {post['user']}'s post!")
            st.markdown(f"**Likes:** {post['likes']} **Comments:** {len(post['comments'])} **Shares:** {post['shares']}")
            for c in post['comments']:
                st.markdown(f"<div class='comment-reply'>{c}</div>",unsafe_allow_html=True)
            st.markdown("</div>",unsafe_allow_html=True)
            st.markdown("---")
            time.sleep(0.05)

# ----------------------
# Chat Page
# ----------------------
elif page=="Chat" and st.session_state.current_user:
    user = st.session_state.users[st.session_state.current_user]
    st.sidebar.subheader("Friends")
    friends_list = user["friends"]
    selected_chat = st.sidebar.selectbox("Select Friend to Chat", [""] + friends_list)

    if selected_chat:
        chat_key = tuple(sorted([st.session_state.current_user, selected_chat]))
        if chat_key not in st.session_state.chat_history:
            st.session_state.chat_history[chat_key] = []

        st.subheader(f"Chat with {selected_chat}")
        for msg in st.session_state.chat_history[chat_key]:
            sender,content,timestamp=msg
            align="left" if sender!=st.session_state.current_user else "right"
            color="#0078d4" if sender==st.session_state.current_user else "#333"
            st.markdown(f"<div style='text-align:{align}; background-color:{color}; padding:0.5rem; border-radius:8px; margin:0.3rem'>{sender} ({timestamp}): {content}</div>",unsafe_allow_html=True)

        new_msg=st.text_input("Type a message", key=f"msg_{selected_chat}")
        if st.button("Send", key=f"send_{selected_chat}") and new_msg.strip():
            st.session_state.chat_history[chat_key].append((st.session_state.current_user,new_msg,time.strftime("%H:%M:%S")))
            st.experimental_rerun()

# ----------------------
# Profile Page
# ----------------------
elif page=="Profile" and st.session_state.current_user:
    user = st.session_state.users[st.session_state.current_user]
    st.subheader("Edit Profile")
    new_avatar = st.text_input("Avatar URL", value=user["avatar"])
    new_bio = st.text_area("Bio", value=user["bio"])
    new_pass = st.text_input("Change Password", type="password")
    if st.button("Save Changes"):
        user["avatar"] = new_avatar
        user["bio"] = new_bio
        if new_pass.strip():
            user["password"] = new_pass
        st.success("Profile updated!")

# ----------------------
# Feed Page with Real-Time Notifications
# ----------------------
elif page=="Feed" and st.session_state.current_user:
    user = st.session_state.users[st.session_state.current_user]

    # Sidebar
    st.sidebar.header(f"{st.session_state.current_user}'s Profile")
    st.sidebar.image(user["avatar"])
    st.sidebar.markdown(f"**Bio:** {user['bio']}")
    if st.sidebar.button("Logout"):
        st.session_state.current_user=None
        st.experimental_rerun()

    # ----------------------
    # Real-time Notifications
    # ----------------------
    st.sidebar.subheader("Notifications")
    notif_container = st.sidebar.container()
    with notif_container:
        if st.session_state.notifications:
            for n in st.session_state.notifications[::-1]:
                st.markdown(f"- {n}")
        else:
            st.markdown("No notifications")

    if st.sidebar.button("Clear Notifications"):
        st.session_state.notifications.clear()
        st.experimental_rerun()

    # ----------------------
    # Real-time Friend Requests
    # ----------------------
    st.sidebar.subheader("Friend Requests")
    fr_container = st.sidebar.container()
    with fr_container:
        if user["requests"]:
            for req in user["requests"]:
                col1, col2 = st.sidebar.columns([2,1])
                col1.markdown(f"Friend request from **{req}**")
                if col2.button(f"Accept {req}"):
                    user["friends"].append(req)
                    st.session_state.users[req]["friends"].append(st.session_state.current_user)
                    user["requests"].remove(req)
                    st.session_state.notifications.append(f"You are now friends with {req}")
                    st.experimental_rerun()
        else:
            st.markdown("No friend requests")

    # Send Friend Request
    st.sidebar.subheader("Send Friend Request")
    potential_friends = [u for u in st.session_state.users if u not in user["friends"] and u != st.session_state.current_user and u not in user["requests"]]
    new_friend = st.sidebar.selectbox("Select user", [""] + potential_friends)
    if st.sidebar.button("Send Request") and new_friend:
        st.session_state.users[new_friend]["requests"].append(st.session_state.current_user)
        st.sidebar.success(f"Friend request sent to {new_friend}")
        st.experimental_rerun()  # Auto-update in real-time

    # ----------------------
    # Post Creation
    # ----------------------
    st.subheader("📣 Create a Post")
    post_text=st.text_area("What's on your mind?")
    post_image_url=st.text_input("Image URL (optional)","")
    if st.button("Post"):
        if post_text.strip()!="":
            post={"user":st.session_state.current_user,"avatar":user["avatar"],"content":post_text,"image":post_image_url if post_image_url else choice(sample_images),"likes":0,"comments":[],"shares":0,"time":time.strftime("%Y-%m-%d %H:%M:%S")}
            st.session_state.posts.insert(0,post)
            # Add notifications for all friends
            for f in user["friends"]:
                st.session_state.notifications.append(f"{st.session_state.current_user} posted a new status!")
            st.success("Posted!")
            st.experimental_rerun()

    # ----------------------
    # News Feed
    # ----------------------
    st.subheader("📰 News Feed")
    feed_container = st.container()
    for idx, post in enumerate(st.session_state.posts):
        if post["user"]!=st.session_state.current_user and post["user"] not in user["friends"]:
            continue
        with feed_container:
            st.markdown(f"<div class='feed-card'>",unsafe_allow_html=True)
            col1,col2=st.columns([1,5])
            with col1: st.image(post["avatar"], width=50)
            with col2:
                st.markdown(f"**{post['user']}** • {post['time']}")
                st.write(post["content"])
                if post["image"]: st.image(post["image"])
            col_like,col_comment,col_share=st.columns([1,2,1])
            with col_like:
                if st.button(f"👍 Like {idx}"):
                    st.session_state.posts[idx]['likes']+=1
                    for f in user["friends"]:
                        st.session_state.notifications.append(f"{st.session_state.current_user} liked {post['user']}'s post!")
                    st.experimental_rerun()
            with col_comment:
                comment_input=st.text_input(f"💬 Comment {idx}", key=f"comment_{idx}")
                if st.button(f"Add Comment {idx}") and comment_input.strip():
                    st.session_state.posts[idx]['comments'].append(f"{st.session_state.current_user}: {comment_input}")
                    for f in user["friends"]:
                        st.session_state.notifications.append(f"{st.session_state.current_user} commented on {post['user']}'s post!")
                    st.experimental_rerun()
            with col_share:
                if st.button(f"🔁 Share {idx}"):
                    st.session_state.posts[idx]['shares']+=1
                    for f in user["friends"]:
                        st.session_state.notifications.append(f"{st.session_state.current_user} shared {post['user']}'s post!")
                    st.experimental_rerun()
            st.markdown(f"**Likes:** {post['likes']} **Comments:** {len(post['comments'])} **Shares:** {post['shares']}")
            for c in post['comments']:
                st.markdown(f"<div class='comment-reply'>{c}</div>",unsafe_allow_html=True)
            st.markdown("</div>",unsafe_allow_html=True)
            st.markdown("---")

# ----------------------
# Real-time 1-on-1 Chat
# ----------------------
if page == "Chat" and st.session_state.current_user:
    user = st.session_state.users[st.session_state.current_user]

    st.sidebar.header(f"{st.session_state.current_user}'s Chat")
    
    # Select friend to chat with
    chat_with = st.sidebar.selectbox("Select a friend", [""] + user["friends"])
    
    # Initialize messages storage
    if "messages" not in st.session_state:
        st.session_state.messages = {}

    if chat_with:
        chat_key = tuple(sorted([st.session_state.current_user, chat_with]))
        if chat_key not in st.session_state.messages:
            st.session_state.messages[chat_key] = []

        st.subheader(f"Chat with {chat_with}")

        # Display messages
        chat_container = st.container()
        for msg in st.session_state.messages[chat_key]:
            align = "right" if msg["from_user"] == st.session_state.current_user else "left"
            st.markdown(f"<div style='text-align:{align}; background-color:#1f1f1f; padding:5px; margin:5px; border-radius:8px;'>{msg['from_user']}: {msg['content']} <small style='color:#888'>{msg['timestamp']}</small></div>", unsafe_allow_html=True)

        # Input new message
        new_msg = st.text_input("Type a message...", key=f"chat_input_{chat_with}")
        if st.button("Send", key=f"send_btn_{chat_with}") and new_msg.strip():
            st.session_state.messages[chat_key].append({
                "from_user": st.session_state.current_user,
                "to_user": chat_with,
                "content": new_msg.strip(),
                "timestamp": time.strftime("%H:%M:%S")
            })
            st.experimental_rerun()  # Real-time effect
