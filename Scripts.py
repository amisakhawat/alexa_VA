import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import requests


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_commad():

    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa","")
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_commad()
    if "play" in command:
        song = command.replace("play","")
        talk("playing..." + song)
        print(pywhatkit.playonyt(song))
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk(f"current time is {time}")

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif "location" in command:
        info = wikipedia.geosearch(48.109840,11.476990)
        talk(info)

    elif "weather" in command:
        info = webbrowser.open("https://www.google.com/search?q=weather+in+my+location&oq=weather+in+&aqs=chrome.1.69i57j0i67i457j0i20i263l2j0l2j69i60l2.5105j1j7&sourceid=chrome&ie=UTF-8")
        info1 = command.replace("weather", "")
        print(info)
        talk(info1)

    elif "what about" in command:
        talk("Sakhawat Hossain is a bangladeshi descent and now living in munich, germany")

    elif "date" in command:
        talk("sorry I am not feeling well, I have a headache")

    elif"are you single" in command:
        talk("no, I am currently in a relationship with Aaminur")

    elif "joke" in command:
        talk(pyjokes.get_joke())
        print(pyjokes)

    else:
        print("please say it again ")

while True:

    run_alexa()
