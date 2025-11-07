import streamlit as st
from random import choice
import time

if st.session_state.current_user is None:
    st.error("Please log in first!")
    st.stop()

user = st.session_state.users[st.session_state.current_user]
sample_images = [
    "https://picsum.photos/400/200?random=1",
    "https://picsum.photos/400/200?random=2"
]

st.title("📰 Feed")
post_text = st.text_area("What's on your mind?")
post_image_url = st.text_input("Image URL (optional)")

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

st.subheader("Your Feed")
for idx, post in enumerate(st.session_state.posts):
    if post["user"] != st.session_state.current_user and post["user"] not in user["friends"]:
        continue
    st.markdown(f"**{post['user']}** • {post['time']}")
    st.write(post["content"])
    if post["image"]:
        st.image(post["image"])
