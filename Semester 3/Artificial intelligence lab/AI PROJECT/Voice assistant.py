import pywhatkit as kit
import speech_recognition as sr
import pyttsx3
import wikipedia
from datetime import datetime
import os

p = pyttsx3.init()  
rate = p.getProperty('rate') #Here rate is a instance and we are getting property which is builted in pyttsx3 and we are getting rate property just to change the speed of voice.
p.setProperty('rate',200)  #Here we are setting the speed of voice to 200
def speak(text):
    p.say(text)  #Say is a built in function it will say what the text we will pass in this function.
    p.runAndWait() 

def listen():  
    recognizer = sr.Recognizer() #Here Recognizer() class creates an object that helps us to retrieve information from a source
    with sr.Microphone() as source:  
        print("Listening...")
        try:
            audio = recognizer.listen(source,timeout = 5)  #This listen function listens to what we say and captures in our microphone and saves the command in the variable.
            user_order = recognizer.recognize_google(audio)  
            print(user_order)
            return user_order.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand what you said. Please say it again")
            return ""

def perform_task(user_order):
    if "how are you" in user_order:
        speak("I am doing great")
        speak("How may i help you")
    

    elif "time" in user_order:
        time = datetime.now().strftime("%I:%M") 
        print(f"The current time is: {time}.")
        speak(f"The current time is {time}.")
        speak("Anyother thing you want to do")

    elif "date" in user_order:
        date = datetime.now().strftime("%B %d")  
        print(f"Today's date is: {date}.")
        speak(f"Today's date is {date}.")
        speak("Anyother thing you want to do")

    elif "search" in user_order:
        speak("What you are searching for?") 
        query = listen()  
        if query:
            kit.search(query)  
            speak(f"Searching for {query}.")
            speak("Anyother thing you want to do")

    elif "play" in user_order:
        speak("Which video should I play?")
        video = listen()   
        if video:
            kit.playonyt(video)
            speak(f"Playing {video} on YouTube.")
            speak("Anyother thing you want to do")

    elif "give me some lines on the topic" in user_order:
        speak("What topic should I search on Wikipedia?")  
        topic = listen()    
        if topic:
                search = wikipedia.summary(topic, sentences=2)
                print(f"According to Wikipedia, {search}")
                speak(f"According to Wikipedia, {search}")
        speak("Anyother thing you want to do")

    elif "open" in user_order:
        if "notepad" in user_order:
            os.system("notepad")
            speak("Opening Notepad.")
            speak("Anyother thing you want to do")
        elif "google" in user_order or "browser" in user_order:
            os.system("start chrome")
            speak("Opening Google.")
            speak("Anyother thing you want to do")
        elif "calculator" in user_order:
            os.system("start calc")
            speak("Opening calculator")
            speak("Anyother thing you want to do")
        elif "whatsapp" in user_order:
            os.system("start whatsapp://")
            speak("Opening whatsapp")
            speak("Anyother thing you want to do")
        elif "settings" in user_order:
            os.system("start ms-settings:")
            speak("Opening settings")
            speak("Anyother thing you want to do")
        else:
            speak("Sorry, I can't open that application.")
            speak("Anyother thing you want to do")

    elif "exit" in user_order or "quit" in user_order or "no thank you" in user_order:
        speak("OK, Let me know if you need further help.")
        speak("Have a good day!")
        exit()

    else:
        speak("I didn't understand that command. Can you try again?")

# Main loop
speak("Hello! I am your voice assistant. How are you?")
while True:
    user_command = listen()
    if user_command:
        perform_task(user_command)


