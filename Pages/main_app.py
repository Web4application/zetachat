import streamlit as st
from random import choice
import time

if "current_user" not in st.session_state:
    st.experimental_set_query_params(page="login")
    st.experimental_rerun()

user = st.session_state.users[st.session_state.current_user]

# Sidebar
st.sidebar.header(f"{user['name']}'s Profile")
st.sidebar.image(user["avatar"])
st.sidebar.markdown(f"**Bio:** {user['bio']}")
st.sidebar.subheader("Friends")
for f_email in user["friends"]:
    friend = st.session_state.users[f_email]
    st.sidebar.markdown(f"- {friend['name']}")

if st.sidebar.button("Logout"):
    st.session_state.current_user = None
    st.experimental_set_query_params(page="login")
    st.experimental_rerun()

# Timeline / Feed
st.title("📰 Timeline")
post_text = st.text_area("What's on your mind?")
if st.button("Post"):
    if post_text.strip():
        post = {
            "user": user["name"],
            "content": post_text,
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": 0,
            "comments": [],
            "shares": 0,
            "avatar": user["avatar"]
        }
        user["posts"].insert(0, post)
        st.success("Posted!")

# Show Posts
for friend_email in [st.session_state.current_user] + user["friends"]:
    friend = st.session_state.users[friend_email]
    for post in friend["posts"]:
        st.markdown(f"<div class='feed-card'>", unsafe_allow_html=True)
        st.image(post["avatar"], width=50)
        st.markdown(f"**{post['user']}**  •  {post['time']}")
        st.write(post["content"])
        st.markdown(f"**Likes:** {post['likes']}  **Comments:** {len(post['comments'])}  **Shares:** {post['shares']}")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("---")
