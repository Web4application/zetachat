import streamlit as st
import time
from random import choice, randint

# ===============================
# 🖤 Dark Modern CSS
# ===============================
dark_css = """
body {
    background-color: #1a1a1a;
    color: #f0f0f0;
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}
.stApp {
    background-color: #1a1a1a;
}
h1, h2, h3, h4, h5, h6 {
    color: #ffffff;
}
div.stButton > button {
    background-color: #4caf50;
    color: white;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-weight: 600;
    transition: background-color 0.2s ease-in-out;
}
div.stButton > button:hover {
    background-color: #45a049;
}
.stTextInput > div > div > input, .stTextArea textarea {
    background-color: #2b2b2b;
    color: #f0f0f0;
    border-radius: 6px;
    border: 1px solid #444;
}
.feed-card {
    background-color: #2b2b2b;
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 1rem;
    box-shadow: 0 0 8px rgba(0,0,0,0.5);
}
.comment-reply {
    background-color: #1f1f1f;
    color: #ccc;
    border-left: 3px solid #4caf50;
    padding: 0.5rem;
    margin: 0.3rem 0;
    border-radius: 4px;
}
::-webkit-scrollbar {
    width: 10px;
}
::-webkit-scrollbar-thumb {
    background-color: #4caf50;
    border-radius: 10px;
}
::-webkit-scrollbar-track {
    background: #1a1a1a;
}
"""

st.markdown(f"<style>{dark_css}</style>", unsafe_allow_html=True)

# ===============================
# 🧠 Mock Database
# ===============================
if "users" not in st.session_state:
    st.session_state.users = {
        "admin": {"password":"admin", "avatar":"https://i.pravatar.cc/50?img=1", "bio":"Hello! I'm admin.", "friends":["user1"], "requests":[]},
        "user1": {"password":"1234", "avatar":"https://i.pravatar.cc/50?img=2", "bio":"I am user1.", "friends":["admin"], "requests":[]}
    }

if "current_user" not in st.session_state:
    st.session_state.current_user = None

if "posts" not in st.session_state:
    st.session_state.posts = []

if "messages" not in st.session_state:
    st.session_state.messages = {}  # {("user1","user2"): [{"sender":"user1","msg":"hello"}]}

if "notifications" not in st.session_state:
    st.session_state.notifications = []

sample_images = [
    "https://picsum.photos/400/200?random=1",
    "https://picsum.photos/400/200?random=2",
    "https://picsum.photos/400/200?random=3",
    "https://picsum.photos/400/200?random=4"
]

# ===============================
# 🔐 Authentication Functions
# ===============================
def login(username, password):
    if username in st.session_state.users and st.session_state.users[username]["password"] == password:
        st.session_state.current_user = username
        st.success(f"Logged in as {username}")
    else:
        st.error("Invalid username or password")

def signup(username, password):
    if username in st.session_state.users:
        st.error("Username already exists")
    else:
        avatar_url = f"https://i.pravatar.cc/50?img={randint(5,70)}"
        st.session_state.users[username] = {"password": password, "avatar": avatar_url, "bio":"New user bio", "friends":[], "requests":[]}
        st.success("Account created! Please log in.")

# ===============================
# 🌐 App Layout
# ===============================
st.set_page_config(page_title="ZetaChat", layout="wide")
st.title("⚡ ZetaChat")

# ---------- Login / Signup ----------
if st.session_state.current_user is None:
    col1, col2 = st.columns(2)
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
    user = st.session_state.users[st.session_state.current_user]

    # ---------- Sidebar Navigation ----------
    st.sidebar.header(f"{st.session_state.current_user}'s Menu")
    menu = st.sidebar.radio("Navigate:", ["Home","Create Post","Friends","Chat","Notifications","Profile"])
    if st.sidebar.button("Logout"):
        st.session_state.current_user = None
        st.experimental_rerun()

    # ===============================
    # 📰 Home Feed
    # ===============================
    if menu == "Home":
        st.subheader("📰 News Feed")
        for idx, post in enumerate(st.session_state.posts):
            if post["user"] != st.session_state.current_user and post["user"] not in user["friends"]:
                continue
            with st.container():
                st.markdown(f"<div class='feed-card'>", unsafe_allow_html=True)
                col1, col2 = st.columns([1,5])
                with col1:
                    st.image(post["avatar"], width=50)
                with col2:
                    st.markdown(f"**{post['user']}**  •  {post['time']}")
                    st.write(post["content"])
                    if post["image"]:
                        st.image(post["image"])
                col_like, col_comment, col_share = st.columns([1,2,1])
                with col_like:
                    if st.button(f"👍 Like {idx}"):
                        st.session_state.posts[idx]['likes'] += 1
                        st.session_state.notifications.append(f"{st.session_state.current_user} liked {post['user']}'s post!")
                with col_comment:
                    comment_input = st.text_input(f"💬 Comment {idx}", key=f"comment_{idx}")
                    if st.button(f"Add Comment {idx}") and comment_input.strip():
                        st.session_state.posts[idx]['comments'].append(f"{st.session_state.current_user}: {comment_input}")
                        st.session_state.notifications.append(f"{st.session_state.current_user} commented on {post['user']}'s post!")
                with col_share:
                    if st.button(f"🔁 Share {idx}"):
                        st.session_state.posts[idx]['shares'] += 1
                        st.session_state.notifications.append(f"{st.session_state.current_user} shared {post['user']}'s post!")
                st.markdown(f"**Likes:** {post['likes']}   **Comments:** {len(post['comments'])}   **Shares:** {post['shares']}")
                for c in post['comments']:
                    st.markdown(f"<div class='comment-reply'>{c}</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("---")
                time.sleep(0.05)

    # ===============================
    # ✍️ Create Post
    # ===============================
    elif menu == "Create Post":
        st.subheader("📣 Create a Post")
        post_text = st.text_area("What's on your mind?")
        post_image_url = st.text_input("Image URL (optional)", "")
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
                st.experimental_rerun()

    # ===============================
    # 👥 Friends
    # ===============================
    elif menu == "Friends":
        st.subheader("👥 Friends")
        st.write("Your Friends:")
        for f in user["friends"]:
            st.markdown(f"- {f}")
        st.write("Friend Requests:")
        for req in user["requests"]:
            col1, col2 = st.columns([2,1])
            col1.write(req)
            if col2.button(f"Accept {req}"):
                user["friends"].append(req)
                st.session_state.users[req]["friends"].append(st.session_state.current_user)
                user["requests"].remove(req)
                st.success(f"You are now friends with {req}")
                st.experimental_rerun()
        st.write("Send Friend Request:")
        potential = [u for u in st.session_state.users if u not in user["friends"] and u != st.session_state.current_user and u not in user["requests"]]
        new_friend = st.selectbox("Select user", [""] + potential)
        if st.button("Send Request") and new_friend:
            st.session_state.users[new_friend]["requests"].append(st.session_state.current_user)
            st.success(f"Friend request sent to {new_friend}")

    # ===============================
    # 💬 Chat
    # ===============================
    elif menu == "Chat":
        st.subheader("💬 Chat")
        if not user["friends"]:
            st.info("Add friends to start chatting.")
        else:
            chat_friend = st.selectbox("Select Friend:", user["friends"])
            chat_key = tuple(sorted([st.session_state.current_user, chat_friend]))
            if chat_key not in st.session_state.messages:
                st.session_state.messages[chat_key] = []
            for msg in st.session_state.messages[chat_key]:
                st.markdown(f"**{msg['sender']}**: {msg['msg']}")
            new_msg = st.text_input("Type a message:")
            if st.button("Send Message") and new_msg.strip():
                st.session_state.messages[chat_key].append({"sender": st.session_state.current_user, "msg": new_msg})
                st.experimental_rerun()

    # ===============================
    # 🔔 Notifications
    # ===============================
    elif menu == "Notifications":
        st.subheader("🔔 Notifications")
        if not st.session_state.notifications:
            st.info("No notifications yet.")
        else:
            for n in st.session_state.notifications[::-1]:
                st.markdown(f"- {n}")
            if st.button("Clear Notifications"):
                st.session_state.notifications.clear()

    # ===============================
    # 🧑 Profile
    # ===============================
    elif menu == "Profile":
        st.subheader("🧑 Profile")
        st.image(user["avatar"], width=100)
        new_bio = st.text_area("Edit Bio:", value=user["bio"])
        if st.button("Save Profile"):
            user["bio"] = new_bio
            st.success("Profile updated!")
