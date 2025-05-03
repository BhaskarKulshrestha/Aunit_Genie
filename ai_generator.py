# import ollama

# # Function to create a prompt from extracted ABAP logic
# def build_prompt(extracted_abap_code):
#     # Customize this prompt based on the specific ABAP logic
#     prompt = f"""
#     Generate AUnit test cases for the following ABAP report code:
#     {extracted_abap_code}
#     """
#     return prompt

# # Function to call Ollama model and generate test case output
# def call_ollama(prompt):
#     try:
#         # Use ollama.chat for interacting with the model (ensure 'llama3' is a valid model)
#         response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])

#         # Debug: Print the full response to understand its structure
#         print("Ollama response:", response)

#         # Access the 'content' key inside the message to get the text response
#         if hasattr(response, 'message') and 'content' in response.message:
#             return response.message['content']
#         else:
#             return f"Unexpected response format: {response}"

#     except Exception as e:
#         return f"Error during AI processing: {str(e)}"


import streamlit as st
from abap_parser import extract_abap_logic
from ai_generator import build_prompt, call_ollama
import random
import time

st.title("🧠 Gen AI - AUnit Test Case Generator for ABAP Reports")

code = st.text_area("Paste ABAP Report Code", height=300)
uploaded_file = st.file_uploader("Or upload .abap/.txt file", type=["abap", "txt"])

funny_quotes = [
    "Compiling... like a coder waiting for coffee ☕️",
    "Hold on! Even AI needs a snack break 🍕",
    "Don't worry, I made the AI wear glasses for better logic 🤓",
    "Turning ABAP into test gold... slowly... but awesomely 💎",
    "The ABAP gods are thinking... probably arguing too 👻",
]

if st.button("Generate AUnit Test Case"):

    if uploaded_file:
        abap_code = uploaded_file.read().decode("utf-8")
    elif code:
        abap_code = code
    else:
        st.error("Please paste or upload ABAP code.")
        st.stop()

    # Show a random funny quote
    status_placeholder = st.empty()
    quote = random.choice(funny_quotes)
    status_placeholder.info(quote)

    # Simulate progress bar
    progress_bar = st.progress(0)
    for percent in range(0, 70, 10):
        time.sleep(0.2)
        progress_bar.progress(percent)

    # Step 1: Parse ABAP
    extracted = extract_abap_logic(abap_code)

    # Step 2: Create prompt
    prompt = build_prompt(extracted)

    # Step 3: Call AI (simulate progress while waiting)
    result = call_ollama(prompt)

    # Complete progress
    for percent in range(70, 101, 10):
        time.sleep(0.1)
        progress_bar.progress(percent)

    # Remove placeholder after done
    status_placeholder.empty()

    # Step 4: Show result
    st.subheader("🧪 AUnit Test Case Output")
    st.code(result, language='abap')

    # Step 5: Download option
    st.download_button("Download Test Code", result, file_name="aunit_test.abap")
    
# This is a simple Streamlit app that allows users to paste or upload ABAP code,