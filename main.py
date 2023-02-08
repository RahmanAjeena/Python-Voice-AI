import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()

engine.setProperty('voice', 'en-us')
engine.setProperty('rate', 150)

with sr.Microphone() as source:
    print("[Powerde On] Say something:")
    audio = r.listen(source)

text = r.recognize_google(audio)

if text == "beta":
  engine.say("works")

engine.runAndWait()
