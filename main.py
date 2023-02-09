import speech_recognition as sr
import pyttsx3
from datetime import datetime
import pywhatkit
import requests
import webbrowser
from config import *
import os

# Weather AI

ow = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=0c42f7f6b53b244c78a418f4f181282a&units=metric"
response = requests.get(ow)
data = response.json()
main = data['main']
tem = main['temp']
temp_feel_like = main['feels_like']

# TIME & DATE
time_now = datetime.now()
current_time = time_now.strftime("%H:%M:%S")
now = datetime.datetime.now()

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
  audbot("Playing the requested video/song")
  video = text.replace('play', '')
  pywhatkit.playonyt(video)
elif 'temperature' in text:
  audbot(f"The temperature is {tem} celsius, and the feel like is {temp_feel_like} celsius")
elif 'date' in text:
    talk(f'Today is ' + now.strftime("%Y-%m-%d"))
else:
  audbot("Error 404")
