# import streamlit as st
# from abap_parser import extract_abap_logic
# from ai_generator import build_prompt, call_ollama

# st.title("🧠 Gen AI - AUnit Test Case Generator for ABAP Reports")

# # Create a text area for pasting code
# code = st.text_area("Paste ABAP Report Code", height=300)

# # File uploader for ABAP or text files
# uploaded_file = st.file_uploader("Or upload .abap/.txt file", type=["abap", "txt"])

# # Button to trigger the test case generation
# if st.button("Generate AUnit Test Case"):
#     if uploaded_file:
#         # If file is uploaded, read its content
#         abap_code = uploaded_file.read().decode("utf-8")
#     elif code:
#         # If code is pasted, use that content
#         abap_code = code
#     else:
#         st.error("Please paste or upload ABAP code.")
#         st.stop()

#     # Step 1: Parse ABAP Code using abap_parser (assuming it's implemented)
#     extracted = extract_abap_logic(abap_code)

#     # Step 2: Build the prompt for the AI model
#     prompt = build_prompt(extracted)

#     # Step 3: Call Ollama AI to generate AUnit test cases
#     result = call_ollama(prompt)

#     # Step 4: Display the generated AUnit test case code
#     st.subheader("🧪 AUnit Test Case Output")
#     st.code(result, language='abap')

#     # Step 5: Provide download button for the test code
#     st.download_button("Download Test Code", result, file_name="aunit_test.abap")


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
