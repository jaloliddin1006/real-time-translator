## translator

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator
import clipboard

root = Tk()
root.title("Translator")
root.geometry("500x500")
root.resizable(False, False)
root.config(bg="black")

# Functions
def translate():
    word = entry.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation = translator.translate(word, dest="en")
    label1.config(text=f"Translated Word: {translation.text}")
    
def clear():
    entry.delete(0, END)
    label1.config(text="Translated Word: ")

def copy():
    text = label1.cget("text")
    clipboard.copy(text)
    messagebox.showinfo("Success", "Text Copied!")

# Frames
frame1 = Frame(root, bg="black")
frame1.pack(pady=20)

frame2 = Frame(root, bg="black")
frame2.pack(pady=20)

frame3 = Frame(root, bg="black")
frame3.pack(pady=20)

# Entry
entry = Entry(frame1, font=("Arial", 20), width=20)
entry.pack()

# Buttons
button1 = Button(frame2, text="Translate", font=("Arial", 20), command=translate)
button1.pack(side=LEFT, padx=10)

button2 = Button(frame2, text="Clear", font=("Arial", 20), command=clear)
button2.pack(side=LEFT, padx=10)

button3 = Button(frame3, text="Copy", font=("Arial", 20), command=copy)
button3.pack()

# Label
label1 = Label(root, text="Translated Word: ", font=("Arial", 20), bg="black", fg="white")
label1.pack(pady=20)

root.mainloop()

# Path: setup.py
## setup

