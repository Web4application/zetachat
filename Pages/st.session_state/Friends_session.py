def show_friends():
    st.title("👥 Active Friends")
    
    # Custom CSS for glowing indicator
    st.markdown("""
        <style>
        .glow {
            width: 10px; height: 10px; background-color: #2ecc71;
            border-radius: 50%; display: inline-block;
            box-shadow: 0 0 8px #2ecc71; margin-right: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    friends = ["Alex", "Jordan", "Taylor"]
    for friend in friends:
        st.markdown(f"<div><span class='glow'></span>{friend} is online</div>", unsafe_allow_html=True)
