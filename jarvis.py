import pyttsx3 #pip install pyttsx3
import datetime
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr #pip install speakRecognition
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("good Evening!")
    speak("Hi,i'm Jarvis mam. Please tell me how may i help you")

def takeCommand():
    #it takes microphone input from the user and gives string as output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshhold = 1
        audio=r.listen(source)

    try:
        print("recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return None
    return query

# To send email
def sendEmail(to,content):
    server = smtplib.smtp("smtp.gmail.com",587)
    server.ehlo()
    sever.starttls()
    server.login("youremail@gmail.com","your-password")
    server.sendmail("youremail@gmail.com",to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing tasks based on query
        if "wikipedia" in query:
            speak("searching wikipedia..")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com") 

        elif "play music" in query:
            music_dir = 'E:\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam,the time is {strtime}")
        elif "open code" in query:
            codepath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(codepath)
        elif "email to shreya" in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "youremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent mam!")
            except Exception as e:
                # print(e)
                speak("sorry mam I am unable to send the email!")

