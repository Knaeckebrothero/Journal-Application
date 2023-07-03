import streamlit as st
from datetime import datetime

# Set config to always start with wide layout
st.set_page_config(layout="wide")

# Main title
st.title('Today is the {} welcome to your digital diary!'
         .format(datetime.today().strftime('%d.%m.%Y')))

activities, rate, write = st.tabs(
    ["Specify your activities...", "Rate your day!", "Wanna mention something else?"])

# Start of by rating the day on a scale from 1 to 10.
with rate.form(key='my_form'):
    st.header('How was your day?')
    overall_rating = st.slider('Overall', 1, 10, 5, key='or')
    emotional_rating = st.slider('Emotional', 1, 10, 5, key='er')
    mental_rating = st.slider('Mental', 1, 10, 5, key='mr')
    st.form_submit_button(label='Rate Me!')
