<div align="center">
  <img width="300" height="300" src="https://em-content.zobj.net/thumbs/120/whatsapp/352/studio-microphone_1f399-fe0f.png">
 </div>
 
# AI-voice-assistant
The AI voice assistant is created as "*part of the Hands on python workshop conducted in 2021-2022*" for high-school students of U.A.E in Ajman University to train on python 
language starting from basics to advanced topics which is used to develop The chatbot.
The application is a web app 

## Table of contents
* [Features](#features)
* [Technologies](#technologies)
* [A Guide to Installation and Use](#a-guide-to-installation-and-use)
* [Web App Architecture](#web-app-architecture)

## Features
The application is designed to listen to user commands once the **record** button is clicked on the **Use it page** which is confirmed by the chatbot voice-output "recording". 
The Communication with the chatbot is always confirmed by the chatbot such that when the command is not clear,noisy, lower volume or the user was at distance from the microphone
it will speak back to user "I did not get that". The interaction with the chatbot continues untill user exists the conversation with one of the exit commands. The full conversation
with the chatbot is documented on the webpage as chat conversation/dialog.
### 1. Greetings
You can greet the assistant by using from of greetings : `hi` , `hello`,`hey`  and the chatbot great you back. <br>
Worth noting, the voice recognition feature is trained on the english language hence the english names prefered.
### 2.  Set User/Assistant Name for the conversation
You can set the assistant name using the command :`your name should be` `< insert assistant name >` <br>
The chatbot confirms the assistant name captured in the microphone as : okay, i will remember that my name is `< insert assistant name >` <br>
You can set the user name using the command :`my name is` ` <insert user name>`
The chatbot confirms the user name captured in the microphone as : okay, i will remember that `< insert user name >` <br>

### 3. Tell the time
Obtaining the current time activated using any of the commands :`what's the time`,`tell me the time
`,`what time is it`,`what is the time` then the chatbot will response with  `The time is` `<current time>`

### 4. Search on Google
The chatbot is designed to search for key terms and sentences on google such as gold prices, stock status <br>
Search for keywords/sentences on google e.g. `search for` `<insert search term/sentence >` and the chatbot will response
with `Here is what I found for machine learning on google` followed by automatically opening internet browser with the results 
of the search

### 5. Search on Youtube
The chatbot is designed to search for key terms and sentences on youtube <br>
Search for keywords/sentences on youtube e.g. `search for` `<insert search term/sentence >` `on youtube` and the chatbot will response
with `Here is what I found for machine learning on youtube` followed by automatically opening internet browser with the results 
of the search on youtube

### 6. Get the weather forcast for the day
What is the weather today e.g. `<sentence>` `weather` for the chatbot will automatically open information about the weather today at your location

### 7. Find location
The chatbot retrieves the user location when user uses the command `what is my exact location`

### 8. Exit the conversation
Using the following terms indicate the end of the conversation with the bot: `bye`,`quit`,`done`,`exit`

## Technologies
The developement is mainly using python language for front-end and back-end as the workshop discusses the python-based development.
Recognizing the voice commands of users is implemeneted using [speech recognition API library](https://pypi.org/project/SpeechRecognition/), and [pyttsx3](pip install pyttsx3) for speaking the output audio. Moreover, the web app is built using [streamlit](https://streamlit.io/) open-source app framework. <br>
The following table summarizes the technologies/libraries used along with its versions:
| **Libarary**       	| **Version** 	|
|--------------------	|-------------	|
| [PyAudio](https://pypi.org/project/PyAudio/) 	| 3.8.1       	|
| [speech_recognition](https://pypi.org/project/SpeechRecognition/)	| 3.8.1       	|
| [pyttsx3](https://pypi.org/project/pyttsx3/)            	| 2.90        	|
| [streamlit](https://pypi.org/project/streamlit/)          	| 1.19.0      	|
| [streamlit_chat](https://pypi.org/project/streamlit-chat/)     	| 0.0.2.2     	|
| [folium](https://pypi.org/project/folium/)             	| 0.14.0      	|
| [streamlit_folium](https://pypi.org/project/streamlit-folium/)   	| 0.11.1      	|
| [st_annotated_text](https://pypi.org/project/st-annotated-text/)  	| 4.0.0       	|
| [pandas](https://pypi.org/project/pandas/)             	| 1.5.3       	|

## A Guide to Installation and Use
Make sure all libraries included in the above table and their dependencies are installed using pip or conda command on your virtual environment.
```
pip install PyAudio
pip install SpeechRecognition 
pip install pyttsx3
pip install streamlit
pip install streamlit-chat
pip install folium
pip install streamlit-folium
pip install st-annotated-text
pip install pandas
```

To run the application, open the terminal in the root directory and exexcute the following command
```
streamlit run HomePage.py 
```

## Web App Architecture
The application consists of mainly four pages:
- **HomePage** : is the landing page , mainly describes the Workshop 
- **User Guide**: documentations of the implementation, where users undertand the valid interactions between users and the web app
- **Use it** : playground page of the chatbot , where user can try/test the voice assistant chatbot 
- **AIRC** : Artificial Intelligence Research Center page 
```
AI-voice-assistant
├── HomePage
│   ├── User Guide
│   ├── Use it
└── └── AIRC
```
