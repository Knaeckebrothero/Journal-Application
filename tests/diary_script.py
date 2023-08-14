import streamlit as st
import json
import os
from datetime import datetime as dt
from tests.pages import rate_page, write_page
from tests.pages import activities_page


def load_day():
    # Check if session state exists
    if 'today' not in st.session_state:
        # Check if today's file exists
        filename = f"diary_{dt.today().strftime('%d%m%Y')}.json"
        filepath = './entries/' + filename
        if os.path.exists(filepath):
            # Load the 'today' dictionary from the JSON file
            with open(filepath, 'r') as f:
                st.session_state.today = json.load(f)
        else:
            # Initialize 'today' dictionary
            st.session_state.today = {"date": dt.today().strftime('%d-%m-%Y'),
                                      "changelog": [],
                                      "important": [],
                                      "activity": [],
                                      "rating": {},
                                      "comment": None,
                                      }


# Config & initialisation
st.set_page_config(layout="wide", page_title="My Diary", initial_sidebar_state="collapsed")
diary_container = st.container()
page_container = st.container()
load_day()

with diary_container:
    # Main title
    st.title(
        'Today is the {} welcome to your digital diary'.format(
            dt.strptime(st.session_state.today["date"],
                        '%d-%m-%Y').strftime('%d.%m.%Y')))
    # Columns for changing the date and saving the day
    col1, col2 = st.columns([1, 1])
    col1.date_input(
            'If you want to change the date please do so, if not simply continue...',
            label_visibility="collapsed",
            value=dt.strptime(st.session_state.today['date'],
                              '%d-%m-%Y')).strftime('%d-%m-%Y')
    col2.button("Save the day!")

# Split application into tabs
activities, rate, write = st.tabs(
    ["What did you do today?",
     "Rate your day!",
     "Wanna mention something?"])

with activities:
    activities_page.activities()

with rate:
    rate_page.rate()

with write:
    write_page.write()
