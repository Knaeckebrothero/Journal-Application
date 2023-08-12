import streamlit as st
from datetime import datetime as dt
import os
import json


def organize():
    # Save the day
    if st.button("Save the day!"):
        # Add a new entry to the changelog
        st.session_state.today["changelog"].append(
            f"Day saved on {dt.now().strftime('%d-%m-%Y %H:%M:%S')}")

        # Create the directory if it doesn't exist
        if not os.path.exists('./entries/'):
            os.makedirs('./entries/')

        # Save the 'today' dictionary as a JSON file
        filename = f"diary_{st.session_state.today['date'].replace('-', '')}.json"
        with open('./entries/' + filename, 'w') as f:
            json.dump(st.session_state.today, f)

        st.success(f"Day saved as {filename}!")

    # Select date for diary entry
    st.session_state.today['date'] = st.date_input(
        'If you want to change the date please do so, if not simply continue...',
        value=dt.strptime(st.session_state.today['date'],
                          '%d-%m-%Y')).strftime('%d-%m-%Y')
