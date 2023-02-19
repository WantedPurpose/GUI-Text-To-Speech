#pip install tk
#pip install pyttsx3

from tkinter import *
import pyttsx3

def speek():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text.get())
    engine.runAndWait()
    text.delete(0, END)


#running

window = Tk()
window.title("Text To Speech")
window.geometry("500x500")
Label(window, text="Enter Yout text",
    font=("Helvetica", 15)).pack(fill="both", pady=20)

text = Entry(window, font=("Helvetica", 15))
text.pack(fill="both", pady=20, padx=10)

btn = Button(window, text="Speak",
             font=("Helvetica", 10), command=speek)
btn.pack(pady=20)

window.mainloop()
