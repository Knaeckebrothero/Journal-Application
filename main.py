import streamlit as st
from datetime import datetime as dt


# Config & initialisation
st.set_page_config(layout="wide", page_title="My Diary")
today = {"date": dt.today(),
         "activity": [],
         "ratings": {},
         "comment": {},
         }

# Main title
st.title('Today is the {} welcome to your digital diary'
         .format(dt.today().strftime('%d.%m.%Y')))

# Split application into tabs
activities, rate, write, organize = st.tabs(
    ["What did you do today?", "Rate your day!", "Wanna mention something?", "Manage your diary."])

# Import tabs content/functionalities
with activities:
    # Holds information about the daily activities
    activity_name = st.text_input(
        'Activity', key='activity_name', value='Activity name')
    activity_start = st.time_input(
        'Start time', key='activity_start', value=dt.now())
    activity_end = st.time_input(
        'End time', key='activity_end', value=dt.now())

    # Checkbox to indicate if activity is ongoing
    ongoing = st.checkbox('Ongoing activity')

    # Tag your activity
    activity_tag = st.selectbox('Tag your activity',
                                ['Study', 'Work',
                                 'Gaming', 'Free time',
                                 'Sport', 'Housekeeping',
                                 'Other'], index=6)

    # Spacing to make it look nicer
    st.markdown('<br/>', unsafe_allow_html=True)

    # Button to add a new activity
    if st.button("Add activity"):
        if ongoing:
            today["activity"].append(
                {"activity": activity_name,
                 "start": activity_start,
                 "end": None,
                 "tag": activity_tag})
        else:
            today["activity"].append(
                {"activity": activity_name,
                 "start": activity_start,
                 "end": activity_end,
                 "tag": activity_tag})

    # Add space at the end
    for _ in range(6):
        st.markdown('<br/>', unsafe_allow_html=True)

with rate:
    # Sliders and diagram
    col1, col2 = st.columns(2)

    # Sliders used to judge different activities
    with col1:
        # Subtitle and description
        st.header("How would you judge your...")

        # Sliders
        focus = st.slider("ability to stay focused during study or work.", 1, 5, 3)
        starting_mood = st.slider("mood at the start of the day.", 1, 5, 3)
        ending_mood = st.slider("mood at the end of the day.", 1, 5, 3)
        satisfaction = st.slider("satisfaction with what you have achieved today.", 1, 5, 3)

    # Create the pie chart in the second column.
    with col2:
        focus_comment = st.text_input("Anything you wanna mention?")

    # Subtitle and description
    st.header("Tag your day using these!")
    # Checkboxes for tagging the day.
    tags = st.multiselect(
        "Tag your day!", label_visibility='collapsed', help="Select all that apply",
        options=['productive', 'relaxed',
                 'meeting', 'university',
                 'friends', 'colleagues', 'family', 'partner',
                 'happy', 'sad', 'exited', 'tired', 'depressed',
                 'junk food', 'busy',
                 'hot', 'cold', 'rainy'], key='tags')

    # Add space at the end
    st.markdown('<br/>', unsafe_allow_html=True)

with write:
    st.header("Is there anything else you wanna mention or comment on?")
    comment = st.text_area("Write here!", label_visibility='hidden', height=300, max_chars=500, key='comment')

    # Add space at the end
    for _ in range(8):
        st.markdown('<br/>', unsafe_allow_html=True)

with organize:
    # Save the day
    if st.button("Save the day!"):
        pass

    # Select date for diary entry
    today = st.text_input('If you want to change the date please do so, if not simply continue...', 
                          value=dt.today().strftime('%d.%m.%Y'),
                          max_chars=None, key=None, type='default')
