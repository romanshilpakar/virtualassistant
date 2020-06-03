import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour >=0 and hour <12:
    speak("Good Morning!")
  
  elif hour >=12 and hour <18:
    speak("Good afternoon!")

  else:
    speak("Good Evening!")

  speak("Hello I am Roman. How can i help you?")

def takeCommand():
  #take microphonw input and return as a string output
     
    r = sr.Recognizer()
    with sr.Microphone() as source:   
      print("Listening....")
      r.pause_threshold = 1.5
      r.energy_threshold = 400 
      audio = r.listen(source)

    try:  
      print("Recognizing...")
      query = r.recognize_google(audio, language= 'en-US')
      print("You Said : ", query) 

    except Exception as e:      
      #print(e)
      print("Sorry, Please say it again.")
      return "None"  
    return query

if __name__ == "__main__":
 wishMe()
 while True:
     
     query = takeCommand().lower()                      
     if  'how are you' in query:
      speak("I am fine what about you?")

     elif  'your name' in query:
      speak("I am Roman")
     
     elif 'wikipedia' in query:
       speak('Searching Wikipedia.')  
       query = query.replace("wikipedia", "")
       results = wikipedia.summary(query, sentences=3)
       speak("Wikipedia says", results)

     elif 'open youtube' in query:  
       webbrowser.open("youtube.com")

     elif 'open google' in query:  
       webbrowser.open("google.com")  
      
     elif 'open facebook' in query:  
       webbrowser.open("facebook.com")

     elif 'play music' in query:  
       webbrowser.open("facebook.com")

     elif 'the time' in query:  
       str_time = datetime.datetime.now().strftime("%H:%M:%S")
       speak(f"The time is {str_time} Sir")

     elif 'open code' in query:  
       path ="D:\\Program Files\\app\\Microsoft VS Code\\Code.exe"
       os.startfile(path)
