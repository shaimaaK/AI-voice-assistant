
import streamlit as st
import voice_assistant
from streamlit_chat import message
import time

st.set_page_config( layout="wide",page_title="AI Voice Assistant",page_icon='🎙️')
st.title("Test the App")
listen_btn = st.button("Record")
if listen_btn:
    go = 1
    while(go):
        #voice_data = voice_assistant.record_audio("Recording")  # get the voice input
        with st.spinner("Recording User Voice ..."):
            #time.sleep(5)
            voice_data = voice_assistant.record_audio("Recording")
        message(voice_data,is_user=True)
        go=voice_assistant.respond(voice_data)