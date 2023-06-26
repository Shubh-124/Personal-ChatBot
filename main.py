
from hugchat import hugchat
from hugchat.login import Login
import streamlit as st
from streamlit_chat import message
from bardapi import Bard
import os
import json
# Ctrl+C to stop the program
# creating a function to generate response

# Reading the JSON file to fetch token
# with open('credentials.json', 'r') as f:
#     file = json.load(f)
#     token = file['output']

st.set_page_config(layout="wide", page_title='Personal ChatBot')


# Log in to huggingface and grant authorization to huggingchat
sign = Login("baahubali932@gmail.com","Shubh@12")
cookies = sign.login()

# Save cookies to usercookies/<email>.json
sign.saveCookies()



# changing the ui of app

# committing the changes onto app
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

print(st.session_state)
# passing two states in session


def generate_response(prompt):
    # Create a ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
    response = (chatbot.chat(prompt))
    # os.environ['_BARD_API_KEY'] = token
    # bard = Bard()
    # response = bard.get_answer(prompt)
    return response


def get_text():
    input_text = st.text_input("Enter message:", "Hey whatssup?", key='input')
    return input_text


st.title("Personal Tutoring Bot")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


# Accepting user input and store it in generate response
user_input = get_text()
if user_input:
    # passing input to generate
    print(user_input)
    output = generate_response(user_input)
    print(output)
    # as soon as enter is pressed, text will be converted to 'past'
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

# printing in reverse chronological order
# printing the generated output first,then displaying the passed output
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        # changing the reply as user
        message(st.session_state['past'][i], key="user_"+str(i),is_user=True)

