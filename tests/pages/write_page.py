import streamlit as st


def write():
    st.header("Is there anything else you wanna mention or comment on?")
    st.session_state.today['comment'] = st.text_area(
        label="Write here!", label_visibility='hidden',
        height=500, max_chars=1000, placeholder="Heute habe ich...")
    if st.checkbox("Contains important information"):
        st.session_state.today['important_comment'] = True
    else:
        st.session_state.today['important_comment'] = False
