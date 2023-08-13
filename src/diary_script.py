import streamlit as st
import json
import os
from datetime import datetime as dt
from pages import activities_page, rate_page, write_page


def load_day() -> str:
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
            json.dump({"date": dt.today().strftime('%d-%m-%Y'),
                       "activity": [],
                       "rating": {},
                       "comment": None,
                       "important": [],
                       "changelog": [],
                       }, f)
            f.close()
    return filepath


def save_day():
    # Save the day
    with open(load_day(), 'w') as f:
        json.dump(st.session_state.today, f)
        f.close()


# Config & initialisation
st.set_page_config(layout="wide", page_title="My Diary", initial_sidebar_state="collapsed")
diary_container = st.container()
page_container = st.container()

# Load the 'today' dictionary from the JSON file
if 'today' not in st.session_state:
    with open(load_day(), 'r') as f:
        st.session_state.today = json.load(f)

with diary_container:
    # Set page titel
    st.title('Today is the {} welcome to your digital diary'.format(
        st.session_state['date'].strftime('%d.%m.%Y')))


    # Columns for changing the date and saving the day
    col1, col2 = st.columns([1, 1])
    st.session_state.date = col1.date_input(
        'If you want to change the date please do so, if not simply continue.',
        label_visibility="collapsed", value=st.session_state.date)
    if col2.button("Save the day!"):
        save_day()

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

# Save changes to file on rerun
save_day()
