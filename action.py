import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather
import os
import subprocess
import pyautogui
import psutil

def greet_based_on_time():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning, sir"
    elif 12 <= current_hour < 18:
        return "Good afternoon, sir"
    else:
        return "Good evening, sir"

def close_application(application_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if application_name.lower() in proc.info['name'].lower():
            os.kill(proc.info['pid'], 9)
            return True
    return False

def Action(data):
    print("Received data:", data)
    print("Data type:", type(data))
    
    if not isinstance(data, str):
        print("Error: Data is not a string.")
        return "Error: Data is not a string."
    
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is DeskBuddy, you can also call me buddy")
        return "My name is DeskBuddy, you can also call me buddy"

    elif "hello" in user_data or "hye" in user_data:
        greeting = greet_based_on_time()
        text_to_speech.text_to_speech(f"Hello, {greeting}. How can I help you?")
        return f"Hello, {greeting}. How can I help you?"

    elif "good morning" in user_data or "good afternoon" in user_data or "good evening" in user_data:
        greeting = greet_based_on_time()
        text_to_speech.text_to_speech(greeting)
        return greeting

    elif "time now" in user_data:
        current_time = datetime.datetime.now().strftime("%H:%M")
        text_to_speech.text_to_speech(f"The time now is {current_time}")
        return f"The time now is {current_time}"

    elif "play" in user_data:
        song = user_data.replace("play ", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        text_to_speech.text_to_speech(f"Searching and playing {song} on YouTube")
        return f"Searching and playing {song} on YouTube"

    elif "open calculator" in user_data:
        os.system("calc")
        text_to_speech.text_to_speech("Calculator is now open")
        return "Calculator is now open"

    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("YouTube is now ready for you")
        return "YouTube is now ready for you"

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("Google is now ready for you")
        return "Google is now ready for you"

    elif "take note" in user_data:
        note = user_data.replace("take note", "").strip()
        with open("note.txt", "a") as f:
            f.write(note + "\n")
        text_to_speech.text_to_speech("Note taken")
        return "Note taken"

    elif "open" in user_data or "run" in user_data or "start" in user_data:
        application = user_data.replace("open ", "").replace("run ", "").replace("start ", "")
        os.system(f"start {application}")
        text_to_speech.text_to_speech(f"{application} is now open")
        return f"{application} is now open"

    elif "close youtube" in user_data:
        if close_application("msedge"):
            text_to_speech.text_to_speech("YouTube is now closed")
            return "YouTube is now closed"
        else:
            text_to_speech.text_to_speech("YouTube was not open")
            return "YouTube was not open"

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Goodbye, sir. Shutting down.")
        return "Goodbye, sir. Shutting down."

    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("Spotify is now ready for you")
        return "Spotify is now ready for you"

    elif "take screenshot" in user_data:
        pyautogui.hotkey('win', 'shift', 's')
        text_to_speech.text_to_speech("Screenshot tool is activated")
        return "Screenshot tool is activated"
    
    elif "search" in user_data:
        query = user_data.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        text_to_speech.text_to_speech(f"Here are the search results for {query}")
        return f"Here are the search results for {query}"

    elif "increase volume" in user_data:
        os.system("nircmd.exe changesysvolume 2000")
        text_to_speech.text_to_speech("Volume Increased")
        return "Volume Increased"

    elif "decrease volume" in user_data:
        os.system("nircmd.exe changesysvolume -2000")
        text_to_speech.text_to_speech("Volume Decreased")
        return "Volume Decreased"

    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

    else:
        text_to_speech.text_to_speech("Sorry, can you repeat")
        return "Sorry, can you repeat"
