import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore, storage
from dotenv import load_dotenv
import os
import time
from datetime import datetime
from random import randint, choice

# ===============================================
# 🌍 Load Environment Variables
# ===============================================
load_dotenv()
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")
FIREBASE_STORAGE_BUCKET = os.getenv("FIREBASE_STORAGE_BUCKET")

# ===============================================
# 🔥 Firebase Setup
# ===============================================
if not firebase_admin._apps:
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {"projectId": FIREBASE_PROJECT_ID, "storageBucket": FIREBASE_STORAGE_BUCKET})

db = firestore.client()
bucket = storage.bucket()

# ===============================================
# 🎨 Custom ZetaGlow Theme (Unique CSS)
# ===============================================
zetaglow_css = """
<style>
body {
    background: radial-gradient(circle at top, #121212, #0a0a0a);
    color: #e0e0e0;
    font-family: 'Poppins', sans-serif;
}
.stApp {
    background: linear-gradient(180deg, #141414 0%, #0d0d0d 100%);
}
h1, h2, h3, h4, h5 {
    color: #00ffe0;
    text-shadow: 0px 0px 12px rgba(0,255,240,0.4);
}
div.stButton > button {
    background: linear-gradient(90deg, #00ffe0, #0077ff);
    color: black;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1.2rem;
    font-weight: 600;
    transition: 0.3s ease-in-out;
}
div.stButton > button:hover {
    background: linear-gradient(90deg, #0077ff, #00ffe0);
}
.stTextInput > div > div > input, .stTextArea textarea {
    background-color: #1c1c1c;
    color: #00ffe0;
    border: 1px solid #00ffe0;
    border-radius: 6px;
}
.feed-card {
    background-color: #171717;
    border-radius: 10px;
    padding: 1rem;
    margin: 1rem 0;
    box-shadow: 0 0 10px rgba(0,255,255,0.1);
    transition: transform 0.15s;
}
.feed-card:hover {
    transform: scale(1.01);
}
.comment-reply {
    background-color: #0e0e0e;
    border-left: 3px solid #00ffe0;
    color: #b9b9b9;
    padding: 0.5rem;
    border-radius: 5px;
}
::-webkit-scrollbar-thumb {
    background: #00ffe0;
    border-radius: 8px;
}
</style>
"""
st.markdown(zetaglow_css, unsafe_allow_html=True)

# ===============================================
# 🧍 User Session Management
# ===============================================
if "user" not in st.session_state:
    st.session_state.user = None

# ===============================================
# 🔐 Authentication
# ===============================================
def login(email, password):
    users = db.collection("users").where("email", "==", email).get()
    for u in users:
        data = u.to_dict()
        if data["password"] == password:
            st.session_state.user = data
            st.success(f"Welcome {data['username']} 👋")
            return
    st.error("Invalid credentials!")

def signup(username, email, password):
    users = db.collection("users").where("email", "==", email).get()
    if users:
        st.error("User already exists!")
        return
    user_data = {
        "username": username,
        "email": email,
        "password": password,
        "bio": "New to ZetaChat 🌍",
        "avatar": f"https://i.pravatar.cc/150?img={randint(1,70)}",
        "friends": [],
        "created": datetime.now().isoformat()
    }
    db.collection("users").document(email).set(user_data)
    st.success("Account created! Please login.")

# ===============================================
# 🌐 Feed + Chat System
# ===============================================
def create_post(user, content, image=None):
    post = {
        "user": user["username"],
        "avatar": user["avatar"],
        "content": content,
        "image": image,
        "likes": 0,
        "comments": [],
        "shares": 0,
        "timestamp": datetime.now().isoformat()
    }
    db.collection("posts").add(post)
    st.success("Post created!")

def upload_image(file):
    blob = bucket.blob(f"uploads/{file.name}")
    blob.upload_from_file(file)
    blob.make_public()
    return blob.public_url

def send_message(sender, receiver, message):
    chat_id = "_".join(sorted([sender, receiver]))
    msg = {
        "sender": sender,
        "receiver": receiver,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }
    db.collection("chats").document(chat_id).collection("messages").add(msg)

# ===============================================
# 🏠 App Layout
# ===============================================
st.set_page_config(page_title="ZetaChat Cloud", layout="wide")
st.title("🌌 ZetaChat Cloud")

if not st.session_state.user:
    st.subheader("Login or Sign Up")
    tab1, tab2 = st.tabs(["🔑 Login", "🆕 Signup"])
    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            login(email, password)
    with tab2:
        username = st.text_input("Username")
        email_new = st.text_input("Email (Signup)")
        password_new = st.text_input("Password", type="password")
        if st.button("Create Account"):
            signup(username, email_new, password_new)
else:
    user = st.session_state.user
    st.sidebar.image(user["avatar"], width=80)
    st.sidebar.markdown(f"**{user['username']}**")
    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.experimental_rerun()

    st.sidebar.header("Menu")
    choice_page = st.sidebar.radio("Go to", ["Feed", "Chat", "Profile"])

    if choice_page == "Feed":
        st.subheader("📰 News Feed")
        content = st.text_area("What's on your mind?")
        image = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])
        if st.button("Post"):
            image_url = upload_image(image) if image else None
            create_post(user, content, image_url)

        posts = db.collection("posts").order_by("timestamp", direction=firestore.Query.DESCENDING).stream()
        for p in posts:
            post = p.to_dict()
            st.markdown(f"<div class='feed-card'><b>{post['user']}</b><br>{post['content']}</div>", unsafe_allow_html=True)
            if post.get("image"):
                st.image(post["image"], use_container_width=True)

    elif choice_page == "Chat":
        st.subheader("💬 1-on-1 Chat")
        users = [u.id for u in db.collection("users").stream() if u.id != user["email"]]
        chat_with = st.selectbox("Select user", users)
        msg = st.text_input("Type a message")
        if st.button("Send"):
            send_message(user["email"], chat_with, msg)
            st.success("Sent!")

        st.markdown("---")
        chat_id = "_".join(sorted([user["email"], chat_with]))
        messages = db.collection("chats").document(chat_id).collection("messages").order_by("timestamp").stream()
        for m in messages:
            data = m.to_dict()
            align = "right" if data["sender"] == user["email"] else "left"
            st.markdown(f"<div style='text-align:{align};padding:5px;'>{data['sender']}: {data['message']}</div>", unsafe_allow_html=True)

    elif choice_page == "Profile":
        st.subheader("👤 Profile")
        st.image(user["avatar"], width=120)
        bio = st.text_area("Edit your bio", user["bio"])
        if st.button("Save Bio"):
            db.collection("users").document(user["email"]).update({"bio": bio})
            st.success("Updated!")
