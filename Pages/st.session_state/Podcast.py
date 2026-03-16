def show_podcast():
    st.title("🎙️ Podcast Room")
    
    is_subscriber = st.session_state.get("is_paid", False)
    
    if not is_subscriber:
        st.warning("This is a premium feature for paid subscribers.")
        if st.button("Upgrade Now"):
            st.session_state.is_paid = True
            st.rerun()
    else:
        st.success("You are Live! Broadcasting to joined friends.")
        st.audio("https://www.soundhelix.com")
