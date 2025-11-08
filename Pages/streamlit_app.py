import streamlit as st

pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])

st.sidebar.selectbox("Group", ["A","B","C"], key="group")
st.sidebar.slider("Size", 1, 5, key="size")

pg.run()
def store_value(key):
    st.session_state[key] = st.session_state["_"+key]
def load_value(key):
    st.session_state["_"+key] = st.session_state[key]

load_value("my_key")
st.number_input("Number of filters", key="_my_key", on_change=store_value, args=["my_key"])
