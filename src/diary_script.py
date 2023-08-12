import streamlit as st
import json
import os
from datetime import datetime as dt
from pages import activities_page, rate_page, write_page


def load_day() -> str:
    # Create the directory if it doesn't exist
    if not os.path.exists('./entries/'):
        os.makedirs('./entries/')

    filename = f"diary_{st.session_state.today.strftime('%d%m%Y')}.json"
    filepath = './entries/' + filename
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            json.dump({"date": dt.today().strftime('%d-%m-%Y'),
                       "changelog": [],
                       "important": [],
                       "activity": [],
                       "rating": {},
                       "comment": None,
                       }, f)
    return filepath


# Config & initialisation
st.set_page_config(layout="wide", page_title="My Diary", initial_sidebar_state="collapsed")
diary_container = st.container()
page_container = st.container()

# Load the day
if 'today' in st.session_state is None:
    st.session_state.today = dt.today()

# Load the 'today' dictionary from the JSON file
with open(load_day(), 'r') as f:
    st.session_state.today = json.load(f)

with diary_container:
    # Main title
    st.title(
        'Today is the {} welcome to your digital diary'.format(
            dt.strptime(st.session_state.date,
                        '%d-%m-%Y').strftime('%d.%m.%Y')))
    # Columns for changing the date and saving the day
    col1, col2 = st.columns([1, 1])
    col1.date_input(
        'If you want to change the date please do so, if not simply continue.',
        label_visibility="collapsed", value=dt.strptime(
            st.session_state.today['date'], '%d-%m-%Y')).strftime('%d-%m-%Y')
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
