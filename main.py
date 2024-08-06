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
    
    # Display instructions
    st.markdown("""
    ### Please follow these Instructions CloFii:
    1. Click on Find.
    2. Select Advanced Find.
    3. Enter the search word.
    4. Click on the More button.
    5. Choose Reading Highlight.
    6. Select Highlight All.
    7. Click on Find in.
    8. Choose Main Document or Current Selection.
    9. All characters are selected. Change the colour into white from the text section.
    """)
    
# To run this app, save the code in a file, say app.py, and run `streamlit run app.py` in your terminal.
