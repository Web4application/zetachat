import streamlit as st

pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])

st.sidebar.selectbox("Group", ["A","B","C"], key="group")
st.sidebar.slider("Size", 1, 5, key="size")

pg.run()
