import speech_recognition as sr
from win32com.client import Dispatch
import wikipedia
import webbrowser
import os
import requests
from musicplay import music_play as m
from dn import download_image
from ai import artificalAi as ai
print("Jarvis is Running")
def speak(audio):
   speaker = Dispatch('SAPI.Spvoice')
   speaker.Speak(audio)
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        audio=r.listen(source)
    try:
        print("Recozining...")
        query=r.recognize_google(audio, language='en-in')
        print("next")
        print(f"User Said : {query}")
        

    except:
        print("Unable To Recognize..")
        return "None"
    return query


if __name__=="__main__":
 speak("Thanks For using Jarvis")
 while True:
    query=take_command().lower()
    
    
    if 'wikipedia' in query:
       print("Searching Results ")
       try:
          speak("Searching Results")
          query=query.replace("wikipedia","")
          results=wikipedia.summary(query, sentences=3)
          speak("According To Wikipedia")
          print(results)
          speak(results)
       except:
          print("Error")
    elif "open" in query:
       print(f'Opening {query.split()[-1].capitalize} ')
       speak(f'Opening {query.split()[-1]} ')
       
       url=f'{query.split()[-1]}.com'
       path='C:\Program Files\Google\Chrome\Application\chrome.exe'
       webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(path))
       webbrowser.get('chrome').open_new(url)

    elif "music" in query:
       speak("Ok Sure")
       print("Ok Sure")
       m()
       
    elif "download" in query:
       speak("Which Image You Want To Download")
       print("Which Image You Want To Download")
       inp=take_command().lower()
       speak("How many Images")
       print("How many Images:")
       try:
        number_images=take_command().lower()
        print(number_images)
        if(number_images<=19):
           download_image(inp,10)
           speak("Successfully Download")
           
        else:
           speak("Cannot Downlaod more than 19 Images")
           print("Cannot Downlaod more than 19 Images")
       except Exception as e:
          print(e)
          speak("Sorry")
    elif "video" in query:
        try:
           
           query=query.replace("video","")
           query=query.replace("play","")
           query=query.replace(" ","")
           
           print(query)
           url=f"youtube.com/@{query}/videos"
           speak(f"Opening Youtube and Playing {query} video")
           path='C:\Program Files\Google\Chrome\Application\chrome.exe'
           webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(path))
           webbrowser.get('chrome').open_new(url)
           
        
        except:
         print("Error")
         speak("Error opening youtube")
    else:
       try:
         query=query.replace("ai","")
         if "using" in query.split():
            query=query.replace("using","")
         
         
         speak(ai(query))
         
       except:
          print("Sorry Can't Contact With ai")
          speak("Sorry Can't Contact With chatGPT")
     
       

       
          
        



