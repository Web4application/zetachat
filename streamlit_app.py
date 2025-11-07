import streamlit as st
import time
from random import choice, randint

# -------------------- Load CSS --------------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------- Mock Database --------------------
if "users" not in st.session_state:
    st.session_state.users = {
        "admin": {"password":"password", "avatar":"https://i.pravatar.cc/50?img=1", "bio":"Hello! I'm admin.", "friends":["user1"], "requests":[]},
        "user1": {"password":"1234", "avatar":"https://i.pravatar.cc/50?img=2", "bio":"I am user1.", "friends":["admin"], "requests":[]}
    }

if "current_user" not in st.session_state:
    st.session_state.current_user = None

if "posts" not in st.session_state:
    st.session_state.posts = []

if "notifications" not in st.session_state:
    st.session_state.notifications = []

sample_images = [
    "https://picsum.photos/400/200?random=1",
    "https://picsum.photos/400/200?random=2",
    "https://picsum.photos/400/200?random=3",
    "https://picsum.photos/400/200?random=4"
]

# -------------------- Auth Functions --------------------
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

# -------------------- App Layout --------------------
st.set_page_config(page_title="Facebook Lite", layout="wide")
st.title("📘 Facebook Lite")

# ---------- Login / Signup ----------
if st.session_state.current_user is None:
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

# ---------- Main App ----------
else:
    user = st.session_state.users[st.session_state.current_user]

    # --------- Sidebar ----------
    st.sidebar.header(f"{st.session_state.current_user}'s Profile")
    st.sidebar.image(user["avatar"])
    st.sidebar.markdown(f"**Bio:** {user['bio']}")

    if st.sidebar.button("Logout"):
        st.session_state.current_user = None
        st.experimental_rerun()

    st.sidebar.subheader("Notifications")
    for n in st.session_state.notifications[::-1]:
        st.sidebar.markdown(f"- {n}")
    st.sidebar.button("Clear Notifications", on_click=lambda: st.session_state.notifications.clear())

    st.sidebar.subheader("Friends")
    for f in user["friends"]:
        if st.sidebar.button(f"View {f}'s Profile"):
            st.session_state.view_profile = f
            st.experimental_rerun()

    st.sidebar.subheader("Friend Requests")
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
        st.sidebar.markdown("No friend requests")

    # Send friend request
    st.sidebar.subheader("Send Friend Request")
    potential_friends = [u for u in st.session_state.users if u not in user["friends"] and u != st.session_state.current_user and u not in user["requests"]]
    new_friend = st.sidebar.selectbox("Select user", [""]+potential_friends)
    if st.sidebar.button("Send Request") and new_friend:
        st.session_state.users[new_friend]["requests"].append(st.session_state.current_user)
        st.sidebar.success(f"Friend request sent to {new_friend}")

    # --------- Viewing Profile Pages ----------
    view_user = st.session_state.get("view_profile", None)
    if view_user:
        view_data = st.session_state.users[view_user]
        st.subheader(f"{view_user}'s Profile")
        st.image(view_data["avatar"], width=100)
        st.markdown(f"**Bio:** {view_data['bio']}")
        st.markdown("**Posts:**")
        for post in st.session_state.posts:
            if post["user"] == view_user:
                st.markdown(f"<div class='feed-card'>", unsafe_allow_html=True)
                st.markdown(f"**{post['user']}**  •  {post['time']}")
                st.write(post["content"])
                if post["image"]:
                    st.image(post["image"])
                st.markdown(f"**Likes:** {post['likes']}   **Comments:** {len(post['comments'])}   **Shares:** {post['shares']}")
                # Threaded comments
                for c in post['comments']:
                    st.markdown(f"<div class='comment-reply'>{c}</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
        if st.button("Back to Feed"):
            st.session_state.view_profile = None
            st.experimental_rerun()
    else:
        # --------- Create Post ----------
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
                st.session_state.notifications.append(f"{st.session_state.current_user} posted a new status!")
                st.success("Posted!")

        # --------- Feed ----------
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

                # Display likes/comments/shares
                st.markdown(f"**Likes:** {post['likes']}   **Comments:** {len(post['comments'])}   **Shares:** {post['shares']}")
                # Threaded comments
                for c in post['comments']:
                    st.markdown(f"<div class='comment-reply'>{c}</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("---")
                time.sleep(0.05)
