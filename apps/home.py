import streamlit as st


def app():
    st.title("Home")

    if "responses" not in st.session_state:
        st.session_state.responses = []

    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    name = st.text_input("What is your name?", st.session_state["my_input"])
    age = st.text_input("What is your age?", st.session_state["my_input"])
    company = st.text_input("What company do you work at?", st.session_state["my_input"])
    food = st.text_input("What is your favorite food?", st.session_state["my_input"])
    submit = st.button("Submit")
    if submit:
        response = {
            "name": name,
            "age": age,
            "company": company,
            "food": food
        }
        st.session_state.responses.append(response)

    