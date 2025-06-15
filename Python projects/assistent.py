import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

#speech to text/
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing... ")
            Data = recognizer.recognize_google(audio)
            print(Data)
            return Data
        except sr.UnknownValueError:
            print("Not Understand...")


#text to speech/
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    if "hey peter" in sptext().lower():

            while True: 

                    data1 = sptext().lower()

                    if "your name" in data1:
                        name = "my name is peter"
                        speechtx(name)

                    elif "your age" in data1:
                        age = "my age is 20"
                        speechtx(age)

                    elif "time" in data1:
                        time = datetime.datetime.now(). strftime("%I%M%p")
                        speechtx(time)

                    elif "youtube" in data1:
                        speech = "opening youtube"
                        speechtx(speech)
                        webbrowser.open("https://www.youtube.com/")

                    elif "linkedin" in data1:
                        speech = "opening linkedin"
                        speechtx(speech)
                        webbrowser.open("www.linkedin.com/in/keshav-hl-8665122b6")

                    elif "joke" in data1:
                        joke_1 = pyjokes.get_joke(language="en", category="all")
                        print(joke_1)
                        speechtx(joke_1)

                    elif "play song" in data1:
                        add = "D:\music"
                        listsong = os.listdir(add)
                        print(listsong)
                        os.startfile(os.path.join(add,listsong[0]))

                    elif "exit" in data1:
                        speechtx("thank you")
                        break

                    time.sleep(10)
    else:
        print("thank you")