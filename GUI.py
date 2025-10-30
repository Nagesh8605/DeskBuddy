from tkinter import *
from PIL import Image, ImageTk
import action
import speech_to_text
import threading
import os
import time

def send():
    send = entry.get()
    bot = action.Action(send)
    text.delete('1.0', END)  # Clear previous text
    text.insert(END, 'User ---> ' + send + "\n")
    if bot is not None:
        text.insert(END, "BOT ---> " + str(bot) + "\n")
    if bot == "Goodbye, sir. Shutting down.":
        close_all()

def ask():
    while True:
        ask_val = speech_to_text.speech_to_text()
        if ask_val is not None:
            bot_val = action.Action(ask_val)
            text.delete('1.0', END)  # Clear previous text
            text.insert(END, 'User ---> ' + ask_val + "\n")
            if bot_val is not None:
                text.insert(END, "BOT ---> " + str(bot_val) + "\n")
            if bot_val == "Goodbye, sir. Shutting down.":
                close_all()

def del_text():
    text.delete('1.0', "end")

def close_all():
    root.destroy()  # Close the Tkinter application
    os.system("taskkill /f /im code.exe")  # Close VS Code (Windows specific)
    # Add more commands if needed to close other applications

def update_clock():
    now = time.strftime("%H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

# Start the background thread for listening to voice commands
thread = threading.Thread(target=ask)
thread.daemon = True
thread.start()

root = Tk()
root.title("DeskBuddy")
root.attributes("-fullscreen", True)
root.config(bg="#ADD8E6")

# Gradient Frame for header
header_frame = Canvas(root, height=100, width=root.winfo_screenwidth())
header_frame.pack(fill="x")
header_frame.create_rectangle(0, 0, root.winfo_screenwidth(), 100, fill="#3b8d99", outline="")
header_frame.create_rectangle(0, 0, root.winfo_screenwidth(), 50, fill="#6b9ac4", outline="")
header_frame.create_rectangle(0, 0, root.winfo_screenwidth(), 25, fill="#a1c4fd", outline="")

# Title Label
title_label = Label(root, text="DeskBuddy", font=("Comic Sans MS", 48, "bold"), bg="#a1c4fd", fg="#000000")
title_label.place(relx=0.5, rely=0.05, anchor=CENTER)

# Live Clock Label
clock_label = Label(root, font=("Comic Sans MS", 12), bg="#a1c4fd", fg="#FFFFFF")
clock_label.place(relx=0.95, rely=0.05, anchor=E)
update_clock()

# Resize the image to fit better within the frame
img = Image.open("C:\\Users\\nages\\OneDrive\\Desktop\\DeskBuddy\\AdobeStock_164361077-1568x1019.jpg")
img = img.resize((700, 500), Image.LANCZOS)  # Zoomed in more
photo = ImageTk.PhotoImage(img)

# Image Label directly on root
image_label = Label(root, image=photo, bg="#ADD8E6")
image_label.place(relx=0.5, rely=0.35, anchor=CENTER)  # Moved upward

# Adding a text widget with reduced size and moved further down
text = Text(root, font=('Courier', 14, 'bold'), bg="#FFFFFF", fg="#000000", bd=5, relief=GROOVE, wrap=WORD)
text.place(relx=0.5, rely=0.7, anchor=CENTER, width=600, height=130)

# Entry widget
entry = Entry(root, font=('Arial', 16), justify=CENTER, bd=5, relief=GROOVE)
entry.place(relx=0.5, rely=0.83, anchor=CENTER, width=500, height=40)

# Send Button
Button2 = Button(root, text="Send", bg="#2196F3", fg="#FFFFFF", font=('Arial', 14, 'bold'), pady=10, padx=20, bd=3, relief=SOLID, command=send)
Button2.place(relx=0.3, rely=0.91, anchor=CENTER)

# Delete Button
Button3 = Button(root, text="Delete", bg="#F44336", fg="#FFFFFF", font=('Arial', 14, 'bold'), pady=10, padx=20, bd=3, relief=SOLID, command=del_text)
Button3.place(relx=0.5, rely=0.91, anchor=CENTER)

# Close DeskBuddy Button
Button4 = Button(root, text="Close DeskBuddy", bg="#FF6347", fg="#FFFFFF", font=('Arial', 14, 'bold'), pady=10, padx=20, bd=3, relief=SOLID, command=close_all)
Button4.place(relx=0.7, rely=0.91, anchor=CENTER)

# Developed by Nagesh Awachar
footer_label = Label(root, text="Developed by Nagesh Awachar", font=("Comic Sans MS", 12, "italic"), bg="#ADD8E6", fg="#000000")
footer_label.place(relx=0.5, rely=0.98, anchor=CENTER)

root.mainloop()
