import requests
import json
import time
from win32com.client import Dispatch
def speak(str):
 speaker=Dispatch("SAPI.SpVoice")
 speaker.Rate = 0  # Adjust the speed value (default is 1)

 speaker.Speak(str)
print("Running NewsSunao App")
response=requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=6c56b45fe922409cb0023d1202e690ff')
r=response.json()
for index,news in enumerate(r['articles']):
 print(f"{index+1}.Number news is {r['articles'][index]['description']}")
 speak(f"{index+1}.Number news is {r['articles'][index]['description']}")
 time.sleep(1)
else:
 speak("News Completed")
