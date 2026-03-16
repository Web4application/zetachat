import streamlit as st

def show_timeline():
    st.title("🌐 Unified Timeline")
    
    # Mock data representing synced activities
    activities = [
        {"source": "X", "user": "@user123", "content": "Just posted a new dev update!", "type": "write-up"},
        {"source": "Instagram", "user": "user_dev", "content": "https://sample-video.mp4", "type": "video"},
    ]

    for post in activities:
        with st.container(border=True):
            # Tag showing where the post is synced from
            st.caption(f"Synced from: **{post['source']}**")
            if post['type'] == "video":
                st.video("https://www.youtube.com") # Example video
            else:
                st.write(post['content'])
            
            if st.button(f"Post to all socials", key=post['content'][:10]):
                st.success("Successfully broadcasted to linked accounts!")
