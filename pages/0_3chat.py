import streamlit as st

if st.session_state.current_user is None:
    st.error("Please log in first!")
    st.stop()

user = st.session_state.users[st.session_state.current_user]
st.title("💬 Chat")
chat_user = st.selectbox("Chat with:", [""] + user["friends"])

if chat_user:
    msg_input = st.text_input("Type your message", key=f"chat_{chat_user}")
    if st.button("Send", key=f"send_{chat_user}") and msg_input.strip():
        st.session_state.messages.append(f"{st.session_state.current_user} → {chat_user}: {msg_input}")
        st.experimental_rerun()
    st.subheader("Messages")
    for msg in st.session_state.messages:
        if chat_user in msg:
            st.markdown(msg)
