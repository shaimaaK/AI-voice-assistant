
import streamlit as st
from streamlit_chat import message
from annotated_text import annotated_text, annotation

st.set_page_config( layout="wide",page_title="AI Voice Assistant",page_icon='🎙️')



def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")

st.title("User Guide")
st.header("Features Available")

#st.info('You can greet the assistant by using hello, hey, hi', icon="ℹ️")

#1 greetings
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**1. Greetings**")
        annotated_text(('You can greet the assistant by using from of greetings : '),('hi ',"keyword"),("  "),(' hello ',"keyword"),("  "),(' hey ',"keyword") )
    with col2:
        message("Hello siri, how are you",is_user=True)
        message("Hey, what's up?, I'm very well, thanks for asking")

st.markdown("""---""")


#2 set user/assistant name        
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**2. Set User/Assistant Name for the conversation**")
        annotated_text(('You can set the assistant name using the command : '),('your name should be ',"command"),("  "),('[ insert assistant name ]',"keyword" ) )
        annotated_text(('You can set the user name using the command : '),('my name is',"command"),("  "),('[ insert user name ]',"keyword" ) )
    with col2:
        message("Hello my name is Anna, your name should be Cortana",is_user=True)
        message("Okay, i will remember that Anna, okay, i will remember that my name is Cortana")

st.markdown("""---""")

#3 tell the time
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**3. Tell the time**")
        annotated_text(('You can tell the time  e.g. '),('what\'s the time ',"command"),("  "),('tell me the time ',"command") ,("  "),('what time is it ',"command"),("  "),('what is the time ',"command"))

    with col2:
        message("what time is it",is_user=True)
        message("The time is  10:30 ")

st.markdown("""---""")

#4 search on google 
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**4. Search on Google**")
        st.markdown("The chatbot is designed to search for key terms and sentences on google such as gold prices, stock status")
        annotated_text(('Search for keywords/sentences on google  e.g. '),('search for ',"command"),("  "),('[ insert search term/sentence ] ',"keyword"))

    with col2:
        message("Search for machine learning",is_user=True)
        message("Here is what I found for machine learning on google ")

st.markdown("""---""")


#5 search on youtube 
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**5. Search on Youtube**")
        annotated_text(('Search for keywords/sentences on youtube  e.g. '),('search for ',"command"),("  "),('[ insert search term/sentence ] ',"keyword"),("  "),('on youtube ',"command"))

    with col2:
        message("Search for robotics on youtube",is_user=True)
        message("Here is what I found for machine learning on youtube ")

st.markdown("""---""")

#6 forecast the weather 
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**6. Get the weather forcast for the day**")
        annotated_text(('What is the weather today e.g. '),('tell me about / what is ',"sentence"),("  "),('weather ',"keyword"))

    with col2:
        message("What is the weather forcast for today",is_user=True)
        message("Here is what I found for on google")

st.markdown("""---""")

#7 location
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**7. Find location**")
        annotated_text(('Sentence ...',"sentence"),("  "),('what is my exact location ',"keyword"))

    with col2:
        message("what is my exact location ",is_user=True)
        message("You must be somewhere near here, as per Google maps")

st.markdown("""---""")

#7 Exit conversation
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**8. Exit the conversation**")
        annotated_text(('Using the following terms indicate the end of the conversation with the bot'),("  "),('bye ',"keyword"),("  "),('quite ',"keyword"),("  "),('done ',"keyword"),("  "),('exit ',"keyword"))

    with col2:
        message("Thank you bot, bye ",is_user=True)
        message("Bye")