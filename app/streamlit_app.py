import streamlit as st

# --- INITIAL APP CONFIG ---
st.set_page_config(page_title="ZetaChat", layout="wide")

# --- GLOBAL STYLES (Glow & Timeline Tags) ---
st.markdown("""
<style>
    .glow-active {
        width: 12px; height: 12px; background-color: #00ffcc;
        border-radius: 50%; display: inline-block;
        box-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc;
        margin-right: 8px;
    }
    .sync-tag {
        background-color: #262730; color: #ff4b4b;
        padding: 2px 8px; border-radius: 10px;
        font-size: 0.8rem; font-weight: bold; border: 1px solid #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "is_subscriber" not in st.session_state:
    st.session_state.is_subscriber = False

# --- SESSION FUNCTIONS ---

def login_page():
    st.title("🛡️ Welcome to ZetaChat")
    with st.form("login_form"):
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.form_submit_button("Access ZetaChat"):
            if user and pwd: # Simple mock check
                st.session_state.logged_in = True
                st.success(f"Welcome back, {user}!")
                st.rerun()

def timeline_session():
    st.title("📱 Unified Timeline")
    st.info("Synchronized activities across your social handles.")
    
    # Example Synced Post
    with st.container(border=True):
        st.markdown("<span class='sync-tag'>FROM X (TWITTER)</span>", unsafe_allow_html=True)
        st.write("Just launched the new AI trading module on ZetaChat! 🚀")
        st.caption("2 hours ago")
        
    with st.container(border=True):
        st.markdown("<span class='sync-tag'>FROM INSTAGRAM</span>", unsafe_allow_html=True)
        st.video("https://www.youtube.com") # Placeholder
        st.write("Check out my latest travel vlog.")

def friends_session():
    st.title("👥 Social Circles")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Active Friends")
        friends = ["@DevAlpha", "@WebWizard", "@CryptoKing"]
        for f in friends:
            st.markdown(f"<div><span class='glow-active'></span> {f} is active</div>", unsafe_allow_html=True)
            
    with col2:
        st.subheader("Sync New Handles")
        st.button("🔗 Link Discord")
        st.button("🔗 Link Facebook")

def podcast_session():
    st.title("🎙️ Podcast Broadcast")
    if not st.session_state.is_subscriber:
        st.warning("Podcast hosting is reserved for Paid Subscribers.")
        if st.button("Become a Subscriber"):
            st.session_state.is_subscriber = True
            st.rerun()
    else:
        st.success("Your Broadcast Room is READY.")
        st.text_input("Podcast Title", placeholder="Enter room name...")
        st.button("🔴 Start Live Stream")
        st.info("Broadcasting to your glowing active friends...")

def trading_session():
    st.title("💹 AI Trade & Verify")
    mode = st.selectbox("Action", ["Select", "Buy", "Sell"])
    
    if mode != "Select":
        asset = st.text_input(f"What do you want to {mode}?")
        if st.button("Initiate AI Verification"):
            with st.status("AI Agent Analyzing Legitimacy...", expanded=True):
                st.write("1. Verifying asset ownership...")
                st.write("2. Checking global market liquidity...")
                st.write("3. Matching with global partner...")
                st.success("Legitimacy Verified! Merging with Buyer/Seller.")
            st.info("Transaction handed over to Online Agent for final escrow.")

# --- NAVIGATION LOGIC ---
if not st.session_state.logged_in:
    login_page()
else:
    # Defining pages for st.navigation
    pg = st.navigation({
        "Home": [st.Page(timeline_session, title="Timeline", icon="🏠")],
        "Social": [st.Page(friends_session, title="Friends", icon="👥")],
        "Media": [st.Page(podcast_session, title="Podcast", icon="🎙️")],
        "Finance": [st.Page(trading_session, title="AI Trading", icon="💹")]
    })
    
    # Add a logout button to the sidebar
    if st.sidebar.button("Log Out"):
        st.session_state.logged_in = False
        st.rerun()
        
    pg.run()
