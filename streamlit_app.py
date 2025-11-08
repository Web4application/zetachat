import streamlit as st
import time
from random import choice, randint

# ================= Dark-mode CSS =================
dark_css = """
body { background-color: #121212; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; }
h1,h2,h3,h4,h5,h6 { color: #ffffff; }
.stApp { background-color: #121212; }
div.stButton > button { background-color: #1a73e8; color: white; border-radius: 6px; padding:0.5rem 1rem; }
div.stButton > button:hover { background-color: #155ab6; }
.stTextInput>div>div>input, .stTextArea textarea { background-color: #1f1f1f; color: #e0e0e0; border-radius: 6px; }
.feed-card { background-color: #1f1f1f; border-radius: 10px; padding: 1rem; margin-bottom: 1rem; }
.comment-reply { background-color: #121212; border-left: 3px solid #1a73e8; padding:0.4rem 0.8rem; margin:0.3rem 0; border-radius: 4px; }
"""
st.markdown(f"<style>{dark_css}</style>", unsafe_allow_html=True)

# ================= Mock Database =================
if "users" not in st.session_state:
    st.session_state.users = {
        "admin@test.com": {"password": "password", "name":"Admin", "avatar":"https://i.pravatar.cc/50?img=1", "bio":"Hello I'm Admin", "friends":["user1@test.com"], "requests":[]},
        "user1@test.com": {"password": "1234", "name":"User1", "avatar":"https://i.pravatar.cc/50?img=2", "bio":"I am User1", "friends":["admin@test.com"], "requests":[]}
    }
if "current_user" not in st.session_state: st.session_state.current_user = None
if "posts" not in st.session_state: st.session_state.posts = []
if "notifications" not in st.session_state: st.session_state.notifications = []
if "chats" not in st.session_state: st.session_state.chats = {}
if "group_chats" not in st.session_state: st.session_state.group_chats = {"Developers":[],"Designers":[],"Gamers":[]}
sample_images = [f"https://picsum.photos/400/200?random={i}" for i in range(1,6)]

# ================= Pages =================
def show_welcome():
    st.title("Welcome to ZetaChat 🚀")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login"):
            st.session_state.page = "login"
            st.experimental_rerun()
    with col2:
        if st.button("Sign Up"):
            st.session_state.page = "signup"
            st.experimental_rerun()

def show_signup():
    st.header("Sign Up")
    email = st.text_input("Email", key="signup_email")
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=10, max_value=120)
    country = st.text_input("Country")
    gender = st.selectbox("Gender", ["Male","Female","Other"])
    password = st.text_input("Password", type="password")
    if st.button("Create Account"):
        if email in st.session_state.users:
            st.error("Email already exists!")
        else:
            st.session_state.users[email] = {
                "password": password, "name": name, "age": age, "country": country, "gender": gender,
                "avatar": f"https://i.pravatar.cc/50?img={randint(3,70)}", "bio":"New user bio", "friends":[], "requests":[]
            }
            st.success("Account created! Please login.")
            st.session_state.page = "login"
            st.experimental_rerun()

def show_login():
    st.header("Login")
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = st.session_state.users.get(email)
        if user and user["password"] == password:
            st.session_state.current_user = email
            st.success(f"Welcome {user['name']}!")
            st.session_state.page = "timeline"
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")

# ================= Main App Pages =================
def sidebar():
    user = st.session_state.users[st.session_state.current_user]
    st.sidebar.header(f"{user['name']}'s Profile")
    st.sidebar.image(user["avatar"])
    st.sidebar.markdown(f"**Bio:** {user['bio']}")
    st.sidebar.button("Logout", on_click=lambda: logout())

    st.sidebar.subheader("Friends Online")
    for f_email in user["friends"]:
        friend = st.session_state.users[f_email]
        st.sidebar.markdown(f"- {friend['name']} (Online)")

    st.sidebar.subheader("Groups")
    for g in st.session_state.group_chats:
        st.sidebar.markdown(f"- {g} ({len(st.session_state.group_chats[g])} messages)")

    st.sidebar.subheader("Notifications")
    for n in st.session_state.notifications[::-1]:
        st.sidebar.markdown(f"- {n}")
    st.sidebar.button("Clear Notifications", on_click=lambda: st.session_state.notifications.clear())

def logout():
    st.session_state.current_user = None
    st.session_state.page = "welcome"
    st.experimental_rerun()

def show_timeline():
    sidebar()
    user = st.session_state.users[st.session_state.current_user]
    st.header("📰 Timeline")

    # --- New Post ---
    post_text = st.text_area("What's on your mind?", key="new_post")
    post_image_url = st.text_input("Image URL (optional)", key="new_post_img")
    if st.button("Post"):
        if post_text.strip():
            post = {
                "user": st.session_state.current_user, "name": user["name"], "avatar": user["avatar"],
                "content": post_text, "image": post_image_url if post_image_url else choice(sample_images),
                "likes": 0, "comments": [], "shares": 0, "time": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.posts.insert(0, post)
            st.session_state.notifications.append(f"{user['name']} posted a new status!")
            st.experimental_rerun()

    # --- Timeline Posts ---
    for idx, post in enumerate(st.session_state.posts):
        st.markdown(f"<div class='feed-card'>", unsafe_allow_html=True)
        st.markdown(f"**{post['name']}**  •  {post['time']}")
        st.write(post["content"])
        if post["image"]: st.image(post["image"])
        col1, col2, col3 = st.columns([1,2,1])
        with col1:
            if st.button(f"👍 Like {idx}"):
                post["likes"] +=1
                st.session_state.notifications.append(f"{user['name']} liked {post['name']}'s post!")
        with col2:
            comment_input = st.text_input(f"💬 Comment {idx}", key=f"comment_{idx}")
            if st.button(f"Add Comment {idx}") and comment_input.strip():
                post["comments"].append(f"{user['name']}: {comment_input}")
                st.session_state.notifications.append(f"{user['name']} commented on {post['name']}'s post!")
        with col3:
            if st.button(f"🔁 Share {idx}"):
                post["shares"] +=1
                st.session_state.notifications.append(f"{user['name']} shared {post['name']}'s post!")
        st.markdown(f"**Likes:** {post['likes']}  **Comments:** {len(post['comments'])}  **Shares:** {post['shares']}")
        for c in post["comments"]:
            st.markdown(f"<div class='comment-reply'>{c}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("---")

    # --- Chat Section ---
    st.subheader("💬 Chat with Friends")
    friend_list = [st.session_state.users[f]["name"] for f in user["friends"]]
    chat_with = st.selectbox("Select friend to chat", [""]+friend_list)
    msg_input = st.text_input("Message")
    if st.button("Send"):
        if chat_with and msg_input.strip():
            friend_email = [f for f in user["friends"] if st.session_state.users[f]["name"]==chat_with][0]
            key = tuple(sorted([user["name"], chat_with]))
            if key not in st.session_state.chats: st.session_state.chats[key] = []
            st.session_state.chats[key].append(f"{user['name']}: {msg_input}")
            st.experimental_rerun()
    if chat_with:
        key = tuple(sorted([user["name"], chat_with]))
        messages = st.session_state.chats.get(key, [])
        for m in messages:
            st.markdown(f"- {m}")

# ================= Routing =================
if "page" not in st.session_state: st.session_state.page = "welcome"
if st.session_state.page == "welcome": show_welcome()
elif st.session_state.page == "signup": show_signup()
elif st.session_state.page == "login": show_login()
elif st.session_state.page == "timeline": show_timeline()
