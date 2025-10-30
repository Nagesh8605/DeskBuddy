<img width="1920" height="1080" alt="Screenshot 2025-10-30 200626" src="https://github.com/user-attachments/assets/bfbae363-ae3a-4b2d-95e9-336662852bca" />**DeskBuddy – Your Personal Desktop Assistant**

**Overview:**
DeskBuddy is an AI-powered personal desktop assistant built using Python.
It helps automate routine tasks, recognize speech, convert text to speech, and provide weather updates — all through an intuitive and interactive interface.

With DeskBuddy, you can manage your desktop hands-free and make your workflow smarter and faster.

**Features**

-Speech Recognition – Talk to your assistant and get instant responses.
-Text-to-Speech Conversion – Converts system text into clear human-like speech.
-Weather Updates – Get real-time weather information for any city.
-Smart GUI – Simple, clean graphical interface for user interaction.
-Screenshot Capture – Take and save screenshots easily.
-Note Taking – Create and save notes directly from your voice commands.

**Tech Stack**

Programming Language: Python
Libraries Used:
speech_recognition
pyttsx3
tkinter
requests
PIL (Python Imaging Library)
datetime
os, time

**Project Structure**
DeskBuddy/
│
├── action.py
├── GUI.py
├── speech_to_text.py
├── text_to_speech.py
├── weather.py
├── note.txt
├── screenshot.png
├── Ai assistant.png
├── AdobeStock_164361077-1568x1019.jpg
└── __pycache__/

**Installation & Usage**
1️⃣ Clone the repository
git clone https://github.com/yourusername/DeskBuddy.git

2️⃣ Navigate to the project folder
cd DeskBuddy

3️⃣ Install required dependencies
pip install -r requirements.txt

4️⃣ Run the project
python GUI.py

**How It Works**

The GUI acts as the central hub for all actions.

Speech recognition listens to user voice commands and triggers corresponding actions.

Text-to-speech responds with an audible voice output.

Weather module fetches live weather data using an API.

Action scripts perform system-level tasks like note creation, taking screenshots, and more.

**Author**

Nagesh Awachar
 MCA (Data Science) |  Aspiring Data Analyst & Tech Enthusiast
📍 JSPM’s Jayawant Institute of Management Studies, Tathawade
🔗 LinkedIn Profile: www.linkedin.com/in/nageshawachar

**Acknowledgment**

Special thanks to all the open-source contributors and Python library developers who made this project possible.


