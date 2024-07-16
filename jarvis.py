import time
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime 
import os
import cv2
import requests
from requests import get
import wikipedia   
import pywhatkit as kit
import smtplib
import sys
import pyautogui
import instaloader
import psutil

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def time():
    Time= datetime.datetime.now().strftime('%I:%M:%S')
    speak('The current time is')
    speak(Time)
    
def date():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    speak('The current date is')
    speak(day)
    speak(month)
    speak(year)
    
def wishme():
    speak('Welcome back sir!')
    time()
    date()
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I help you?")    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('samaniwahiduddin382@gmail.com','S@mani121921')    
    server.sendmail('samaniwahiduddin382@gmail.com', to, content)  
    server.close()

def weather():
    api_key = "ec50293ddc81ce7bf2bbba628d3b967b"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("Which city weather you want to know?")
    city_name = takeCommand()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature in kelvin unit is " +
            str(current_temperature) +
            "\n humidity in percentage is " +
            str(current_humidity) +
            "\n description  " +
            str(weather_description))
    else:
        speak(" City Not Found ")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
if __name__ == "__main__":
    wishme()
    while True:
    #if 1:
        query = takeCommand().lower()
        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
            
        elif 'weather' in query:
            weather()
            
        elif'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that" + remember.read())
        
        elif 'open notepad' in query:
            path="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(path)
            
        elif "close notepad" in query:
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open command prompt' in query:
            path="C:\\WINDOWS\system32\\cmd.exe"
            os.startfile(path)
            
        elif "close command prompt" in query:
            speak("closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        elif 'open calculator' in query:
            path="C:\\WINDOWS\\system32\\calc.exe"
            os.startfile(path)
            
        elif "close calculator" in query:
            speak("closing calculator")
            os.system("taskkill /f /im calculator.exe")
        

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27: #Esc key to close the camera
                    break;
            cap.release()
            cv2.destroyAllWindows()
        

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
                  

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
            
        elif 'close youtube' in query:
            speak("closing youtube")
            os.system("taskkill /f /im chrome.exe") 

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            
        elif 'close google' in query:
            speak("closing google")
            os.system("taskkill /f /im chrome.exe")        
            
        elif 'send message' in query:
            kit.sendwhatmsg_instantly("+919930810330", "This is a test message") 
            speak("Message has been sent")
            
        elif 'play on youtube' in query:
            speak("What do you want to play?")
            song = takeCommand().lower()
            kit.playonyt(song)
            
        elif 'shutdown system' in query:
            os.system("shutdown /s /t 5")
            
        elif 'restart system' in query:
            os.system("shutdown /r /t 5")
            
        elif 'sleep system' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            
        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
        elif 'instagram profile' in query:
            speak("Please enter the username correctly")
            name = input("Enter username here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Here is the profile of the user {name}")
            time.sleep(5)
            speak("Sir, do you want to download the profile picture of this account?")
            condition = takeCommand().lower()
            if 'yes' in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I have downloaded the profile picture of this account")
            else:
                pass
        
        elif 'take screenshot' in query:
            speak("Sir, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("Please hold the screen for few seconds, I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I have taken the screenshot, Sir")
            
        
        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "natasharai3094@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
                
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")  
                
        elif 'no thanks' in query:
            speak("Thanks for using me. Have a good day")
            sys.exit()
            
        speak("Sir, do you have any other work to do? ")
            
            
            
            
          
              
                
                
            
        

        





        

