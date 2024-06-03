import streamlit as st




def app():
    st.title("Users")    
    st.write("### All Responses:")
    for idx, resp in enumerate(st.session_state.responses, start=1):
        st.write(f"Response {idx}: {resp}")
