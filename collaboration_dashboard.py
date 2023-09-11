import streamlit as st
import time
import json

# Open and read the JSON file
with open('users.json', 'r') as json_file:
    users = json.load(json_file)


# Session data
if 'validateUserID' not in st.session_state:
    st.session_state.validateUserID = ''

# Initialize session state variables
if 'selected_options_1' not in st.session_state:
    st.session_state.selected_options_1 = []
if 'selected_options_2' not in st.session_state:
    st.session_state.selected_options_2 = []
if 'selected_options_3' not in st.session_state:
    st.session_state.selected_options_3 = []
if 'ideas' not in st.session_state:
    st.session_state.ideas = []
if 'newIdea' not in st.session_state:
    st.session_state.newIdea = ''
if 'newCertIdea' not in st.session_state:
    st.session_state.newCertIdea = ''
if 'newBuildIdea' not in st.session_state:
    st.session_state.newBuildIdea = ''

# Test data (to be removed once we connect to Snowflake)
learningList = ['PL/SQL', 'Snowflake', 'AWS', 'Oracle', 'PowerBI', 'Tableau']
certificationList = [
    'AWS Certified Architect Associate', 'Snowflake SnowPro Core',
    'AWS Certified Cloud Practitioner', 'Oracle PL/SQL Developer Certified Associate'
]
projectList = ['AngularJS web application', 'Android mobile app']

def validateUserID():
    # This will check in Snowflake if the user already exists (with a select count to check if exists)
    # Will return True or False based on st.session_state.userId
    if 1 == 1:
        st.session_state.validateUserID = ':heavy_check_mark: Username ' + st.session_state.userId + ' is available'
    else:
        st.session_state.validateUserID = ':x: Username ' + st.session_state.userId + ' is not available. Please enter a new one.'
    return True

# Function to add an idea to the list
def addIdea():
    if st.session_state.newIdea != "":
        st.session_state.ideas.append(st.session_state.newIdea)

def addCertIdea():
    if st.session_state.newCertIdea != "":
        st.session_state.ideas.append(st.session_state.newCertIdea)

def addBuildIdea():
    if st.session_state.newBuildIdea != "":
        st.session_state.ideas.append(st.session_state.newBuildIdea)

with st.container():
    # FMR logo on top - will adjust the align later
    st.image('https://www.fidelity.com/bin-public/060_www_fidelity_com/images/Fidelity-footer-logo.png')
    # Titles and headers
    st.title("Fidelity AMT Learning Days")
    st.divider()
    st.header('Learning Objectives Submission Form')
    st.caption('This tool will assist in finding associates with similar learning interests, enabling collaboration of study groups')
    st.divider()
    st.subheader('Please enter your details:')

with st.container():
    # Input fields
    st.text_input(label="Your preferred User ID", value="", on_change=validateUserID, key='userId')
    st.caption(st.session_state.validateUserID)
    # st.session_state.userId is what needs to be validated
    userName = st.text_input("Your Full Name", "")
    userEmail = st.text_input("Your E-mail", "")
    # Radio button to select which multiselect to show
    selected_radio = st.radio("What are you interested in achieving during Learning Days?",
                             ["Learning :open_book:", "Certification :medal:", "Building a project :desktop_computer:"])

    # Display the selected radio button's corresponding multiselect
    if selected_radio == "Learning :open_book:":
        st.session_state.selected_options_1 = st.multiselect("Choose Learning subject:", learningList,
                                                             st.session_state.selected_options_1)
        # Create a checkbox to add a new learning idea
        add_new_idea = st.checkbox("Add New Learning Idea")
        if add_new_idea:
            st.text_input("Your Idea", on_change=addIdea(), key='newIdea')
    elif selected_radio == "Certification :medal:":
        st.session_state.selected_options_2 = st.multiselect("Choose Certification:", certificationList,
                                                             st.session_state.selected_options_2)
        # Create a checkbox to add a new Certification 
        add_new_idea = st.checkbox("Add New Certification Idea")
        if add_new_idea:
            st.text_input("Your Certification Idea", on_change=addCertIdea, key='newCertIdea')
    else:
        st.session_state.selected_options_3 = st.multiselect("Choose project type to Build:", projectList,
                                                             st.session_state.selected_options_3)
        # Create a checkbox to add a new project 
        add_new_idea = st.checkbox("Add New build Idea")
        if add_new_idea:
            st.text_input("Your build Idea", on_change=addBuildIdea(), key='newBuildIdea')

# Combine selected options from all radio buttons
all_selected_options = (        
        st.session_state.selected_options_1 +
        st.session_state.selected_options_2 +
        st.session_state.selected_options_3 +
        st.session_state.ideas)


# Display the selected options for all the radio buttons
st.divider()
if len(all_selected_options) > 0:
    st.write("You have selected:")
for option in all_selected_options:
    st.write(option)

with st.expander('People with Similar Interests:'):
    with st.spinner('Performing associate matching...'):
        time.sleep(4)
        for option in all_selected_options:
            st.markdown(f'## {option}')
            time.sleep(2)
            found = False
            for user in users:
                if option in user['Interests']:
                    found = True
                    st.write(user['Username'],' ',user['Email'])
                    time.sleep(0.5)
            if not found:
                st.success('Sorry, no associates have been matched to your learning objectives')

            st.divider()
