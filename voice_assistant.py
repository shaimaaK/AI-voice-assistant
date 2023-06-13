# import libraries
import speech_recognition as sr  # recognise speech
import random
from time import ctime  # get time details
import webbrowser  # open browser
import pyttsx3


# Initialization functions
user = 'Siri'
asis = ''


def setUserName(name):
    global user
    user = name


def setAsistantName(name):
    global asis
    asis = name


def there_exists(terms,voice_data):
    for term in terms:
        if term in voice_data:
            return True
    return False



# listen for audio and convert it to text:
def record_audio(ask=""):
    # Listening functions
    r = sr.Recognizer()  # initialise a recogniser
    with sr.Microphone() as source:  # microphone as source
        if ask:
            print("engine is", ask)
            engine_speak(ask)
            print("start listening")
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down')  # error: recognizer is not connected
        print(">>", voice_data.lower())  # print what user said
        return voice_data.lower()

# def record_audio(ask=""):
#     with sr.Microphone() as source:  # microphone as source
#         audio = r.listen(source, 5, 5)  # listen for the audio via source
#         print("Done Listening")
#         voice_data = ''
#         try:
#             voice_data = r.recognize_google(audio)  # convert audio to text
#         except sr.UnknownValueError:  # error: recognizer does not understand
#             engine_speak('I did not get that')
#         except sr.RequestError:
#             engine_speak('Sorry, the service is down')  # error: recognizer is not connected
#         print(">>", voice_data.lower())  # print what user said
#         return voice_data.lower()


# Speaking Functions

# Step1: convert speech to text


def engine_speak(text):
    engine = pyttsx3.init()
    print(text+" .....")
    text = str(text)
    print("must speak now!")
    engine.say(text)  # convert text to audio
    engine.runAndWait()  # speak the audio through speakers


# Step2: Response functionality
def respond(voice_data):
    # 1: greeting
    if there_exists(['hey', 'hi', 'hello'], voice_data):
        greetings = ["hey, how can I help you" + user, "hey, what's up?" + user, "I'm listening" + user,
                     "how can I help you?" + user, "hello" + user]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

    # 2: assistant name
    if there_exists(["what is your name", "what's your name", "tell me your name"],voice_data):

        if user:
            engine_speak(f"My name is {asis}, {user}")  # gets users name from voice input
        else:
            engine_speak(f"My name is {asis}. what's your name?")  # incase you haven't provided your name.

    if there_exists(["your name should be"], voice_data):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        setAsistantName(asis_name)  # remember name in asis variable

    if there_exists(["my name is"], voice_data):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        setUserName(person_name)  # remember name in person variable

    if there_exists(["what is my name"], voice_data):
        engine_speak("Your name must be " + user)

    # 3: greeting
    if there_exists(["how are you", "how are you doing"], voice_data):
        engine_speak("I'm very well, thanks for asking " + user)

    # 4: time
    if there_exists(["what's the time", "tell me the time", "what time is it", "what is the time"], voice_data):
        time = ctime().split(" ")[4].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " and " + minutes + "minutes"
        engine_speak("The time is " + time)

    # 5: search google
    if there_exists(["search for"], voice_data) and 'on youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["on youtube"], voice_data):
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube", "").replace("search", "")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")

    # 7: get stock price
    if there_exists(["price of"], voice_data):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

    # 8 weather
    if there_exists(["weather"], voice_data):
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")

    if there_exists(["exit", "quit", "bye", "done"], voice_data):
        engine_speak("bye")
        return 0

    # 10 Current location as per Google maps
    if there_exists(["what is my exact location"], voice_data):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps")
    return 1