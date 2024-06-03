from streamlit_option_menu import option_menu
import streamlit as st
from apps import home, another_test

st.set_page_config(page_title="Title", layout="centered")
st.write('# Welcome to the SHOW')


apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    {"func": another_test.app, "title": "User List", "icon": "house"},

]


titles = [page["title"] for page in apps]

with st.sidebar:
    selected= option_menu(
        "Main Menu",
        options=titles,
        menu_icon="cast",
    )

    st.sidebar.title("About")

for page in apps:
    if page['title'] == selected:
        page["func"]()
        break

