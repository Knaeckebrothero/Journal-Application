import matplotlib.pyplot as plt
import streamlit as st


# Define sliders
sleep_hours = st.slider("Sleep", 0, 24, 8)
work_hours = st.slider("Work", 0, 24 - sleep_hours, 0)
study_hours = st.slider("Study", 0, 24 - sleep_hours - work_hours, 0)
free_time_hours = 24 - sleep_hours - work_hours - study_hours
st.write("Free Time", free_time_hours)

# Define data for pie chart
activities = ['Sleep', 'Work', 'Study', 'Free Time']
hours = sleep_hours, work_hours, study_hours, free_time_hours
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Create pie chart
fig1, ax1 = plt.subplots()
ax1.pie(hours, labels=activities, colors=colors, autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)


# Start of by rating the day on a scale from 1 to 10.
with st.form(key='my_form'):
    st.header('How was your day?')
    overall_rating = st.slider('Overall', 1, 10, 5, key='or')
    emotional_rating = st.slider('Emotional', 1, 10, 5, key='er')
    mental_rating = st.slider('Mental', 1, 10, 5, key='mr')
    st.form_submit_button(label='Rate Me!')