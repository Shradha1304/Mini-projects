from tkinter import *
import speech_recognition as sr
import pyttsx3 as p
from tkinter import messagebox


root=Tk()
root.title("speech to text and text to speech")
root.geometry('400x500')
root.config(bg="gray")

def speech():
    r = sr.Recognizer()
    messagebox._show(title=None,message="SAY SOMETHING")
    mic = sr.Microphone(device_index=1)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        messagebox._show(title='processing',message="recognizing please wait")
        text = r.recognize_google(audio)
        messagebox._show(title='output', message=text)
def text():
    en = p.init()
    en.say(entry.get())
    en.runAndWait()
    en.delete(0,END)


btn1= Button( text="speech to text", font="segoe 18",highlightcolor='blue', relief=SUNKEN, bd=0, command=speech, fg="white", bg="#333333")
btn1.pack(pady=20)

entry = Entry(root, font="segoe 18")
entry.pack(pady=20)

btn2= Button( text="text to speech", font="segoe 18", relief=RAISED, bd=0, command=text, fg="white", bg="#333333")
btn2.pack(pady=20)
root.mainloop()
