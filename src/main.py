import os
import json
import streamlit as st
from datetime import time
from datetime import datetime as dt


def get_path():
    # Load directory and filename
    filename = f"diary_{st.session_state['date'].strftime('%d%m%Y')}.json"
    filepath = './entries/' + filename
    return filepath


# Load a day
def load_day():
    # Create the directory if it doesn't exist
    if not os.path.exists('./entries/'):
        os.makedirs('./entries/')

    # Load directory and filename
    filepath = get_path()

    # Create the file if it doesn't exist
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            json.dump({
                "date": st.session_state['date'].strftime('%d.%m.%Y'),
                "activity": [],
                "important": [],
                "focus": 3,
                "starting_mood": 3,
                "ending_mood": 3,
                "satisfaction": 3,
                "tags": [],
                "focus_comment": None,
                "start_mood_comment": None,
                "end_mood_comment": None,
                "satisfaction_comment": None,
                "comment": None,
                "important_comment": False,
                "changelog": [],
            }, f)
        f.close()

    # Load the day
    with open(filepath, 'r') as f:
        st.session_state.today = json.load(f)
    f.close()


# Save a day
def save_day():
    # Save the day
    with open(get_path(), 'w') as f:
        json.dump(st.session_state.today, f)
    f.close()


# Main function
if __name__ == '__main__':
    # Config & initialisation
    st.set_page_config(layout="wide", page_title="My Diary", initial_sidebar_state="collapsed")

    # Check if the date is in session state
    if 'date' not in st.session_state:
        st.session_state['date'] = dt.today()

    # Check if today is in session state
    if 'today' not in st.session_state or None:
        load_day()

    if st.session_state['date'].strftime('%d.%m.%Y') != st.session_state.today['date']:
        # Delete today from st.session_state and rerun script to create or load the new day
        st.session_state.today.clear()
        st.experimental_rerun()
    else:
        # Save changes to file on script rerun
        save_day()

    # Set page title
    st.title('Today is the {} welcome to your digital diary'.format(
        st.session_state['date'].strftime('%d.%m.%Y')))

    # Columns for changing the date and saving the day
    col1, col2 = st.columns([1, 1])
    st.session_state.date = col1.date_input(
        'If you want to change the date please do so, if not simply continue.',
        label_visibility="collapsed", value=st.session_state.date)

    # Split application into tabs
    activities, rate, write = st.tabs(
        ["What did you do today?",
         "Rate your day!",
         "Wanna mention something?"])

    with activities:
        # Specify how demanding the activity was.
        activity_category = st.selectbox('Tag based on cognitive demand',
                                         ['Concentration',
                                          'Relaxation',
                                          'Organizational'],
                                         key='activity_category')

        # Enter information about the activity
        activity_description = st.text_input(label='Describe your activity',
                                             key='activity_description',
                                             placeholder='What did you do?')
        activity_start = st.time_input(
            'Start time', key='activity_start', value=time(0, 0))
        activity_end = st.time_input(
            'End time', key='activity_end', value=time(0, 0))

        # Tag your activity
        activity_tags = st.multiselect(
            "Activity was related to",
            options=['Academic', 'Business', 'Hobbies',
                     'Breaks', 'Leisure', 'Exercise',
                     'Housekeeping', 'Personal Care', 'Administrative'],
            key='activity_tags')

        # Spacing to make it look nicer
        st.markdown('<br/>', unsafe_allow_html=True)

        # Button to add a new activity
        if st.button("Add activity"):
            st.session_state.today["activity"].append(
                {"description": activity_description,
                 "start": activity_start.strftime('%H:%M:%S'),
                 "end": activity_end.strftime('%H:%M:%S'),
                 "category": activity_category,
                 "tags": activity_tags})
            st.success("Activity added successfully!")

        # Spacing to make it look nicer
        st.markdown('<br/><br/>', unsafe_allow_html=True)

        important_habit = st.text_input(label='Keep track and test new stuff!',
                                        placeholder='Could be anything like a habit or food supplements...')
        if st.button("Mark today"):
            st.session_state.today['important'].append(important_habit)

    with rate:
        # Sliders and diagram
        col1, col2 = st.columns(2)

        # Sliders used to judge different activities
        with col1:
            # Subtitle and description
            st.header("How would you judge your...")

            # Sliders
            st.session_state.today["focus"] = st.slider(
                "Ability to stay focused throughout the day.", 1, 5, 3)
            st.session_state.today["starting_mood"] = st.slider(
                "Mood at the start of the day.", 1, 5, 3)
            st.session_state.today["ending_mood"] = st.slider(
                "Mood at the end of the day.", 1, 5, 3)
            st.session_state.today["satisfaction"] = st.slider(
                "Satisfaction with what you have achieved today.", 1, 5, 3)

        with col2:
            # Subtitle and description
            st.header("Anything you wanna mention?")

            st.session_state.today["focus_comment"] = st.text_input(
                "Did you feel stressed?", key='focus_comment')

            st.markdown('<br/>', unsafe_allow_html=True)
            st.session_state.today["start_mood_comment"] = st.text_input(
                "What was responsible for this?", key='start_mood_comment')
            st.session_state.today["end_mood_comment"] = st.text_input(
                "What should I write here?", key='end_mood_comment',
                label_visibility='hidden')

            st.markdown('<br/>', unsafe_allow_html=True)
            st.session_state.today["satisfaction_comment"] = st.text_input(
                "What would others say?", key='satisfaction_comment')

        # Subtitle and description
        st.header("Tag your day using these!")

        # Checkboxes for tagging the day.
        st.session_state.today["tags"] = st.multiselect(
            "Tag your day!", label_visibility='collapsed', help="Select all that apply",
            options=['productive', 'relaxed', 'stressful', 'fun',
                     'friends', 'colleagues', 'family', 'partner',
                     'happy', 'sad', 'excited', 'tired', 'depressed',
                     'junk-food', 'thc', 'insomnia', 'dispute',
                     'hot', 'cold', 'rainy'], key='tags')

    with write:
        st.header("Is there anything else you wanna mention or comment on?")
        st.session_state.today['comment'] = st.text_area(
            label="Write here!", label_visibility='hidden',
            height=500, max_chars=1000, placeholder="Heute habe ich...")
        if st.checkbox("Contains important information"):
            st.session_state.today['important_comment'] = True
        else:
            st.session_state.today['important_comment'] = False
