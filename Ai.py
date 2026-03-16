import streamlit as st
import time

# --- CONFIG & STYLES ---
st.set_page_config(page_title="ZetaChat OS", layout="wide")

st.markdown("""
<style>
    .glow { width: 12px; height: 12px; background-color: #00ffcc; border-radius: 50%; 
            display: inline-block; box-shadow: 0 0 15px #00ffcc; margin-right: 10px; }
    .stChatMessage { border-radius: 15px; border: 1px solid #333; }
</style>
""", unsafe_allow_html=True)

# --- BACKEND LOGIC (The "AI" Engine) ---
class ZetaAI:
    @staticmethod
    def verify_trade(asset_details):
        """Simulates an AI Agent verifying a trade."""
        steps = ["Analyzing asset history...", "Checking global liquidity...", "Verifying seller identity..."]
        for step in steps:
            yield step
            time.sleep(1)
            
    @staticmethod
    def sync_socials():
        """Mock function for Social Media Aggregation."""
        return [
            {"platform": "X", "text": "Market is bullish today!", "tag": "Financial"},
            {"platform": "Instagram", "text": "Live from the studio.", "tag": "Media"}
        ]

# --- SESSION STATE ---
if "user_auth" not in st.session_state:
    st.session_state.user_auth = False

# --- PAGES ---
def timeline():
    st.title("🌐 Live Feed")
    posts = ZetaAI.sync_socials()
    for p in posts:
        with st.chat_message("user"):
            st.write(f"**[{p['platform']}]** {p['text']}")
            st.caption(f"Tag: {p['tag']}")

def trading():
    st.title("💹 AI Trade Verifier")
    with st.expander("Initiate New Trade", expanded=True):
        asset = st.text_input("Asset to Trade (e.g., BTC, Stock, Real Estate)")
        if st.button("Run AI Verification"):
            status_container = st.empty()
            for progress in ZetaAI.verify_trade(asset):
                status_container.info(progress)
            st.success(f"Verification Complete for {asset}. Merging with verified global buyer...")
            st.button("Transfer to Agent Escrow")

def friends():
    st.title("👥 Active Network")
    friends_list = ["@ZetaUser_1", "@Alpha_Dev", "@Crypto_Minds"]
    for friend in friends_list:
        st.markdown(f"<div><span class='glow'></span> {friend} - *Streaming Podcast*</div>", unsafe_allow_html=True)

# --- NAVIGATION ---
if not st.session_state.user_auth:
    st.title("ZetaChat Login")
    if st.button("Secure Login with AI"):
        st.session_state.user_auth = True
        st.rerun()
else:
    pg = st.navigation([
        st.Page(timeline, title="Timeline", icon="🗞️"),
        st.Page(friends, title="Circle", icon="👥"),
        st.Page(trading, title="AI Trading", icon="💰")
    ])
    pg.run()
