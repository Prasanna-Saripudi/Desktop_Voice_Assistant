import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

if __name__ == "__main__":

    wake = "arya"
    while True:
        # speak("Hi")
        c = takeCommand().lower()
        print(c)
        if c.count(wake) > 0:
            speak("Hi, What can i do for you?")
            c = takeCommand().lower()
            speak(c)
