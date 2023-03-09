import speech_recognition as sr
import pyttsx3

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}\n")
        return query
    
    except Exception as e:
        print(e)
        speak("Sorry, I didn't understand what you said.")
        return None
