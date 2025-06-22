import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "a8bd7c6b9a9947a9a2f47fb0fd0f5593"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3')
    

#     # Initialize pygame mixer
#     pygame.mixer.init()

#     # Load your MP3 file
#     pygame.mixer.music.load("temp.mp3")  # Replace with your actual file path

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep the program running until the music finishes
#     while pygame.mixer.music.get_busy():
#         continue  # You can also add time.sleep() to reduce CPU usage

#     pygame.mixer.music.load()
#     os.remove("temp.mp3")



# # def aiprocess(command):
# #     client = OpenAI(api_key = "{apikey}")
    
# #     completion = client.chat.completions.create
# #     (
    
# #         model=="gpt-3.5-turbo",
# #         messages=[
# #             {
# #                 "role": "system",
# #                 "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google.Give short responses please"
# #             }
# #             {
# #                 "role": "user",
# #                 "content": command
# #             }
# #         ]
# #     )

# #     return completion.choices[0].message.content
    



# print(completion.choices[0].message.content)


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()  # Convert JSON to Python dict
            
            articles = data.get("articles", [])  # Get list of articles

            # Print the top headlines
            for i, article in enumerate(articles[:5], start=1):  # Limit to first 5
                speak(f"{i}. {article['title']}")

    else:
        # let OpenAI handle the request
        output = aiprocess(c)
        speak(output)





    

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        # Listen for the wake word "Jarvis"
        # Obtain audio from the microphone
        r = sr.Recognizer()
        
        
        
        print("recognizing....")
        # recognizing speech using google
        try:
            with sr.Microphone() as source:
                print("Listning...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source,timeout = 2, phrase_time_limit = 1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command:
                with sr.Microphone() as source:
                    print("Jarvis Activated....")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source,timeout = 2, phrase_time_limit = 1)
                    command = r.recognize_google(audio)

                    processCommand(command)



            
        except Exception as e:
            print("error; {0}".format(e))
        
             