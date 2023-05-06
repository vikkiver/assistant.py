import speech_recognition as sr    #speech recognosier
import datetime
import pyttsx3
import pywhatkit
import webbrowser
import pyjokes

# recognise=sr.Recognizer() 
root=pyttsx3.init()
voices=root.getProperty('voices')
root.setProperty('voice',voices[1].id)


def speak(text):
    root.say(text)
    root.runAndWait()

speak("Hi How can i help you")
def record_audio():
    recognise=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....!")
        recognise.pause_threshold=1
        audio = recognise.listen(source,timeout=60,phrase_time_limit=100)
        recognise.dynamic_energy_threshold=True
    try:
        voice_data = recognise.recognize_google(audio)            # voice to text
        print(voice_data.lower())  
        
    except Exception as e:
        speak("sorry....Unable to recognise your voice")
               
    return voice_data


def response():
    
    if "play" in voice_data:
        song=voice_data.replace("play"," ")
        speak("playing...."+song)
        pywhatkit.playonyt(song)
        
    
    elif "time" in voice_data:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("current time is"+time)
        print(time)


    elif "search" in voice_data:
        search_data=voice_data.split("for")[-1]
        url=f"https://google.com/search?q={search_data}"
        webbrowser.get().open(url)
        speak(f"here is what i found in google about {search_data}")
            

    elif "what" in voice_data:
        search=voice_data.split("is")[-1]
        url=f"https://google.com/search?q={search}"
        webbrowser.get().open(url)
        speak(f"here is what i found about {search} in google")

    elif "who" in voice_data:
        search_term=voice_data.split("is")[-1]
        url=f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f"here is what i found about {search_term} in google")

    elif "joke" in voice_data:
        speak(pyjokes.get_joke())
        print(pyjokes.get_joke())

    elif "exit" in voice_data:
        speak("ok i am going offline")
        print("ok i am going offline")

while True:
        voice_data=record_audio()
        response()