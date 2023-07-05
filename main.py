import streamlit as st
from datetime import datetime
from activities import activities_page
from rate import rate_page
from write import write_page

# Set config to always start with wide layout
st.set_page_config(layout="wide", page_title="My Diary")

# Main title
st.title('Today is the {} welcome to your digital diary!'
         .format(datetime.today().strftime('%d.%m.%Y')))

# Split application into tabs
activities, rate, write = st.tabs(
    ["Specify your activities...", "Rate your day!", "Wanna mention something else?"])

# Import tabs content/functionalities
with activities:
    # Holds information about the daily activities
    activities_page()

with rate:
    # Used to judge the day
    rate_page()

with write:
    # Used to specify additional information
    write_page()
