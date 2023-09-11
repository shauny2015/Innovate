import time
import streamlit as st

# FMR logo on top - will adjust the align later
st.image('https://www.fidelity.com/bin-public/060_www_fidelity_com/images/Fidelity-footer-logo.png')
# Titles and headers
st.title("Fidelity AMT Learning Days")
# Create two columns
col1, col2 = st.columns(2)

# Add content to the first column
with col1:
    st.markdown("Subject: **Snowflake**")
    st.write("*Others with the same interest*")
    st.markdown("* johndoe")
    st.markdown("* davidbrown")
    st.markdown("* emilyjones")
    st.markdown("---")
    # Add more content as needed

# Add content to the second column
with col2:
    st.markdown("**Top 5 Fidelity Learning Resources for ***Snowflake*****")
    st.markdown("---")
    st.write("This is the content for the second column.")
    # Add more content as needed
