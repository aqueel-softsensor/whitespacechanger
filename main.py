import streamlit as st
import pyperclip

# Function to replace spaces with carets
def replace_spaces(input_string):
    return input_string.replace(' ', '^')

# Create the Streamlit app
st.title('Made with Love for my Love ❤️')

# Accept string input from user
input_string = st.text_area('Enter your string:')

# Replace spaces with carets
if input_string:
    formatted_string = replace_spaces(input_string)
    
    # Display formatted output in a text area (text parser)
    st.text_area('Formatted Output:', value=formatted_string, height=150)
    
# To run this app, save the code in a file, say app.py, and run `streamlit run app.py` in your terminal.