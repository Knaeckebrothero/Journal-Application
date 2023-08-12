import streamlit as st


def rate():
    # Sliders and diagram
    col1, col2 = st.columns(2)

    # Sliders used to judge different activities
    with col1:
        # Subtitle and description
        st.header("How would you judge your...")

        # Sliders
        st.session_state.today["rating"]["focus"] = st.slider(
            "Ability to stay focused throughout the day.", 1, 5, 3)
        st.session_state.today["rating"]["starting_mood"] = st.slider(
            "Mood at the start of the day.", 1, 5, 3)
        st.session_state.today["rating"]["ending_mood"] = st.slider(
            "Mood at the end of the day.", 1, 5, 3)
        st.session_state.today["rating"]["satisfaction"] = st.slider(
            "Satisfaction with what you have achieved today.", 1, 5, 3)

    with col2:
        # Subtitle and description
        st.header("Anything you wanna mention?")

        st.session_state.today["rating"]["focus_comment"] = st.text_input(
            "Did you feel stressed?", key='focus_comment')

        st.markdown('<br/>', unsafe_allow_html=True)
        st.session_state.today["rating"]["start_mood_comment"] = st.text_input(
            "What was responsible for this?", key='start_mood_comment')
        st.session_state.today["rating"]["end_mood_comment"] = st.text_input(
            "What should I write here?", key='end_mood_comment',
            label_visibility='hidden')

        st.markdown('<br/>', unsafe_allow_html=True)
        st.session_state.today["rating"]["satisfaction_comment"] = st.text_input(
            "What would others say?", key='satisfaction_comment')

    # Subtitle and description
    st.header("Tag your day using these!")

    # Checkboxes for tagging the day.
    st.session_state.today["rating"]["tags"] = st.multiselect(
        "Tag your day!", label_visibility='collapsed', help="Select all that apply",
        options=['productive', 'relaxed', 'stressful', 'fun',
                 'friends', 'colleagues', 'family', 'partner',
                 'happy', 'sad', 'excited', 'tired', 'depressed',
                 'junk-food', 'thc', 'insomnia', 'dispute',
                 'hot', 'cold', 'rainy'], key='tags')