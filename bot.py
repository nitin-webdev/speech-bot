import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import os
import webbrowser
import time
import requests
import subprocess
import wolframalpha
# import pyscreenshot
# import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

tasks = ["Open You Tube", "Open Gmail", "Open google", "Show time", "Find news",
         "Solve arithmetic and geographical queries (Eg 45/15)", "Predict weather", "help", "Clear screen", "Notepad"]


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 4000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            print(e)
            speak("Pardon me, please say that again")
            return "None"
        return statement


print("Loading your AI personal assistant")
speak("Loading your AI personal assistant")
wish_me()

if __name__ == '__main__':
    while True:
        speak("Tell me how can I help you?")
        command = take_command().lower()
        if command == 0:
            continue

        if "good bye" in command or "ok bye" in command or "stop" in command:
            speak('Good by and have a nice day')
            print('Good by and have a nice day')
            break

        if "wikipedia" in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in command:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in command:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in command:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "clear screen" in command:
            os.system('cls')

        elif "notepad" in command or "open notepad" in command:
            programName = "notepad.exe"
            fileName = "file.txt"
            subprocess.Popen([programName, fileName])

        elif "time" in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print("Current time is " + strTime)

        elif "news" in command:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/")
            speak('Here are some headlines from the Times of India, Happy reading')
            time.sleep(6)

        elif "search" in command:
            command = command.replace("search", "")
            webbrowser.open_new_tab(command)
            time.sleep(5)

        elif "use calculator" in command:
            question = take_command()
            app_id = "876HYT-AGQWG5W4JG"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "solve questions" in command or "solve question" or "have a question" in command:
            speak("Tell me your question")
            question = take_command()
            app_id = "876HYT-AGQWG5W4JG"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "weather" in command:
            api_key = "b146fcc9f98dc66f1a457c11ec454c54"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = take_command()
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
                print(city_name)
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))

        elif "help" in command:
            speak('I am your personal assistant. I am programmed to do some basic tasks')
            for task in tasks:
                index = tasks.index(task)
                print(str(index) + "." + task)

        # elif "take screenshot" in command or "take image" in command:
        #     screenshot = pyautogui.screenshot()
        #     screenshot.save("screen.png")

        elif "who made you" in command or "who created you" in command or "who programmed you" in command:
            speak("I was built by Nitin, Saurabh and dedipya")
            print("I was built by Nitin, Saurabh and dedipya")

        elif "log off" in command or "sign out" in command:
            speak("Ok , your pc will log off in 10 second make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "restart system" in command:
            speak("Your system will restart in 10 second make sure to save all your important work")
            time.sleep(10)
            os.system("shutdown /r /t 30")

