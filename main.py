from tkinter import *
from tkinter import ttk
import os
import wikipedia
import pyjokes


def get_command():
    command = input.get()
    if "code" in command:
        codepath = r"C:\Users\AKSHAT\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(codepath)
    if "brave" in command:
        bravepath = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        os.startfile(bravepath)
    if "wiki" in command:
        commands = command.replace("wiki", "")
        wikiresult = wikipedia.summary(commands, sentences=3)
        ttk.Label(frame, text=wikiresult, wraplength=300, justify="center").grid(column=1, row=5)
    if "joke" in command:
        jokes = pyjokes.get_joke()
        ttk.Label(frame, text=jokes).grid(column=1, row=5)
    

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="Welcome master").grid(column=0, row=0)

input = Entry(frame, bd = 5)
input.grid(column=1, row=1)
ttk.Button(frame, text="Submit", command=get_command).grid(column=2, row=1)
ttk.Button(frame, text="QUIT", command=root.destroy).grid(column=1, row=2)
root.mainloop()