import streamlit as st
from pages.utils.CONFIG import LOGGED_IN_PATH
from pages.utils.helpers import avoid_block_read
# py -m streamlit run C:/Users/timmy/PycharmProjects/AttendanceVK2/Home.py
st.title("Welcome to Team 888's Attendance Page!")
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = avoid_block_read(LOGGED_IN_PATH)


st.header("Getting Started")
st.write(""""

Temp Placeholder

""")

st.header("Features")
st.write("""
Temp placeholder
""")