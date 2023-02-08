import speech_recognition as sr
import pyttsx3
from datetime import datetime
import pywhatkit
import webbrowser
import os

# TIME
time_now = datetime.now()
current_time = time_now.strftime("%H:%M:%S")

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', 'en-us')
engine.setProperty('rate', 150)

with sr.Microphone() as source:
    print("[Powered On]")
    audio = r.listen(source)

text = r.recognize_google(audio)

def audbot(text):
  engine.say(text)
  engine.runAndWait()

if 'time' in text:
  audbot('The Time Is ' + current_time)
elif 'play' in text:
  video = text.replace('play', '')
  pywhatkit.playonyt(video)
else:
  engine.say("Error 404")