import streamlit as st
from datetime import datetime
from pages.activities import activities_page
from pages.rate import rate_page
from pages.write import write_page

# Set config to always start with wide layout
st.set_page_config(layout="wide")

# Main title
st.title('Today is the {} welcome to your digital diary!'
         .format(datetime.today().strftime('%d.%m.%Y')))

activities, rate, write = st.tabs(
    ["Specify your activities...", "Rate your day!", "Wanna mention something else?"])

with activities:
    activities_page()

with rate:
    rate_page()

with write:
    write_page()
