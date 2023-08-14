import os
from datetime import datetime as dt
import streamlit as st
import json


def load() -> str:
    # Create the directory if it doesn't exist
    if not os.path.exists('./entries/'):
        os.makedirs('./entries/')

    # Load the date from the session state
    if 'date' not in st.session_state:
        st.session_state['date'] = dt.today()

    # Load directory and filename
    filename = f"diary_{st.session_state['date'].strftime('%d%m%Y')}.json"
    filepath = './entries/' + filename

    # Create the file if it doesn't exist
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            json.dump({
                "date": dt.today().strftime('%d-%m-%Y'),
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
    return filepath


def save():
    # Save the day
    with open(load(), 'w') as f:
        json.dump(st.session_state.today, f)
        f.close()
