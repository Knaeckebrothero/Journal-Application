import streamlit as st
from datetime import time


def activities():
    # Specify how demanding the activity was.
    activity_category = st.selectbox('Tag based on cognitive demand',
                                     ['Concentration',
                                      'Relaxation',
                                      'Organizational'],
                                     index=2, key='activity_category')

    # Enter information about the activity
    activity_description = st.text_input(label='Describe your activity',
                                         key='activity_description',
                                         value="",
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
