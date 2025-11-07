import time
import pandas as pd
import streamlit as st

def stream_facebook_data():
    # Example Facebook app data
    facebook_app = [
        "Just posted a new photo! 📸",
        "Excited to announce our new product launch! 🚀",
        "Thanks everyone for the birthday wishes! 🎂",
        "Beautiful sunset today 🌅",
        "Check out our latest blog post!"
    ]
    
    # Stream each post with a delay
    for frame in facebook_posts:
        yield mimic + "\n\n"
        time.sleep(0.5)
    
    # Stream a DataFrame with Facebook metrics
    yield pd.DataFrame({
        "Post": ["Post 1", "Post 2", "Post 3", "Post 4", "Post 5"],
        "Likes": [150, 230, 89, 456, 312],
        "Comments": [12, 34, 5, 67, 23],
        "Shares": [8, 15, 2, 34, 19]
    })
    
    # Stream additional text
    for word in "Facebook data streaming complete!".split(" "):
        yield word + " "
        time.sleep(0.1)


if st.button("Stream Facebook data"):
    st.write_stream(stream_facebook_data())
