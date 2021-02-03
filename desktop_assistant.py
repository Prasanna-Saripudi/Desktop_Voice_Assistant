import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wakeup():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 87.4543961958468
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 0.8
        print("Listening...")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')
        except Exception as e:
            print(str(e))
            return "None"
        return statement.lower()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 87.4543961958468
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 0.8
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement.lower()


if __name__ == "__main__":

    wake = "arya"
    while True:
        c = wakeup()
        print(c)
        if c.count(wake) > 0:
            speak("Hi, What can i do for you?")
            query = takeCommand()
            speak("your command is " + query)
