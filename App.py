import streamlit as st

# Title for the app
st.title("Chatbot")

# Input box
user_input = st.text_input("Enter the Question:")

# Button to process the input
if st.button("Process"):
    # Replace this logic with your Google Colab script functionality
    result = f"Processed string: {user_input[::-1]}"  # Example: reversing the string
    st.success(result)
