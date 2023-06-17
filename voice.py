import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hello I am Akshar")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognize.....")
        query=r.recognize_google(audio,language='en-in')
        #speak(query)
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again please.....")
        return "none"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('avats1044@gmail.com','Arpit123#')
    server.sendmail('avats1044@gmail.com',to,content)
    server.close()
if __name__=="__main__":
    wishme()
    while True:
        query =takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'search' in query and 'in youtube' in query:
            query=query.replace('search', '')
            query=query.replace('in youtube', '')
            url='https://www.youtube.com/results?search_query='+query
            webbrowser.open_new(url)
        elif 'search' in query and 'in google' in query:
            query=query.replace('search', '')
            query=query.replace('in google', '')
            #query = "python programming"  # Replace with your query variable
            url = f"https://www.google.com/search?q="+query
            webbrowser.open_new(url)
        elif 'open youtube' in query :
            speak('opening youtube')
            webbrowser.open_new('youtube.com')
        elif 'open python' in query:
            webbrowser.open("coursera.org")
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open_new('google.com')
        elif 'open github' in query:
            webbrowser.open("github.com")   
        elif 'open stackoverflow' in query:
            speak('opening stackoverflow')
            webbrowser.open_new('stackoverflow.com')
        elif 'open spotify' in query :
            speak('opening spotify')
            webbrowser.open_new('spotify.com')
        elif 'thank you' in query:
            speak('my pleasure')
        elif 'close' in query:
            break
        
            
        
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        