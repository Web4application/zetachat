import streamlit as st

if st.session_state.current_user is None:
    st.error("Please log in first!")
    st.stop()

user = st.session_state.users[st.session_state.current_user]
st.title("👤 Profile")
st.image(user["avatar"])
st.markdown(f"**Bio:** {user['bio']}")

st.subheader("Friends")
for f in user["friends"]:
    st.markdown(f"- {f}")

st.subheader("Friend Requests")
for req in user["requests"]:
    col1, col2 = st.columns([2,1])
    col1.markdown(f"{req} wants to be your friend")
    if col2.button(f"Accept {req}"):
        user["friends"].append(req)
        st.session_state.users[req]["friends"].append(st.session_state.current_user)
        user["requests"].remove(req)
        st.experimental_rerun()
