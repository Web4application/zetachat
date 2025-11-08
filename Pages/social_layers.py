import streamlit as st

# Ensure user is logged in
if "current_user" not in st.session_state:
    st.experimental_set_query_params(page="login")
    st.experimental_rerun()

current_user = st.session_state.current_user
user = st.session_state.users[current_user]

# --- Friend Requests ---
st.sidebar.subheader("Friend Requests")
if user["requests"]:
    for req_email in user["requests"]:
        req_user = st.session_state.users[req_email]
        col1, col2 = st.sidebar.columns([2,1])
        col1.markdown(f"Request from **{req_user['name']}**")
        if col2.button(f"Accept_{req_email}"):
            user["friends"].append(req_email)
            req_user["friends"].append(current_user)
            user["requests"].remove(req_email)
            if "notifications" not in st.session_state:
                st.session_state.notifications = []
            st.session_state.notifications.append(f"You are now friends with {req_user['name']}")
            st.experimental_rerun()
        if col2.button(f"Decline_{req_email}"):
            user["requests"].remove(req_email)
            st.experimental_rerun()
else:
    st.sidebar.markdown("No friend requests")

# --- Send Friend Request ---
st.sidebar.subheader("Send Friend Request")
potential_friends = [
    email for email in st.session_state.users 
    if email != current_user and email not in user["friends"] and email not in user["requests"]
]
new_friend = st.sidebar.selectbox("Select user", [""] + potential_friends)
if st.sidebar.button("Send Request") and new_friend:
    st.session_state.users[new_friend]["requests"].append(current_user)
    st.sidebar.success(f"Friend request sent to {st.session_state.users[new_friend]['name']}")

# --- Notifications ---
st.sidebar.subheader("Notifications")
if "notifications" not in st.session_state:
    st.session_state.notifications = []

for n in st.session_state.notifications[::-1]:
    st.sidebar.markdown(f"- {n}")

st.sidebar.button("Clear Notifications", on_click=lambda: st.session_state.notifications.clear())

# --- Online Friends ---
st.sidebar.subheader("Friends Online")
for f_email in user["friends"]:
    friend = st.session_state.users[f_email]
    st.sidebar.markdown(f"- {friend['name']} (Online)")
