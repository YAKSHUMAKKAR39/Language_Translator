import tkinter as tk
import tkinter.font as font
import speech_recognition as sr
from   gtts import gTTS
from translate import Translator
import googletrans
from tkinter import ttk
import os

r = sr.Recognizer()
mic = sr.Microphone()

def language(x, text):
    global t
    translator = Translator(to_lang = x)
    t = translator.translate(text)
    textBox2.insert("1.0", t)

def funRecord():
    global audio
    with mic as source:
        r.adjust_for_ambient_noise(source, duration = 0.3)
        audio = r.listen(source)
        textBox1.insert("1.0",r.recognize_google(audio))

def convert():
    global x
    x = choice.get()
    text = textBox1.get("1.0", tk.END)
    language(x,text)

def hear():
    global obj
    obj = gTTS(text = t, lang = list2[list1.index(x)] , slow = False)
    obj.save("123.mp3")
    os.system("123.mp3")
    

list1 = list(googletrans.LANGUAGES.values())
list2 = list(googletrans.LANGUAGES.keys())

window = tk.Tk( )
window.title("Language-->Translator")
window.configure(bg = "#61CD8E")  # for background color

window.rowconfigure([0,1,2,3,4,5,6,7,8], weight = 1, minsize = 35)
window.columnconfigure([0,1,2,3,4,5,6,7,8], weight = 1, minsize = 35)

label = tk.Label(text = "LANGUAGE => TRANSLATOR", fg = "#11552E" , bg = "#61CD8E",
                 relief = tk.RIDGE, borderwidth = 5, font = "Verdana")
label['font'] = font.Font(size= 18)
label.grid(row = 0, column = 4, pady = 10, ipadx = 5, ipady = 5)

label1 = tk.Label(text = "Translated Message in\nselected language", fg = "#197640", bg = "#61CD8E",
                  relief = tk.RIDGE, borderwidth = 2, font = "Verdana")
label1.grid(row = 1, column = 7, ipadx = 5, ipady = 5)

label1 = tk.Label(text = "You can either type or\n record your message", fg = "#197640", bg = "#61CD8E",
                  relief = tk.RIDGE, borderwidth = 2, font = "Verdana")
label1.grid(row = 1, column = 1, ipadx = 5, ipady = 5)

labelSelect = tk.Label(text = "Select language", fg = "white", bg = "#24A158",
                    relief = tk.RIDGE, borderwidth = 3, font = "Verdana")
labelSelect.grid(row = 2, column = 4, ipadx = 5, ipady = 5)
inst = tk.StringVar()
choice = ttk.Combobox(window, width = 15, textvariable = inst)
choice['values'] = list1
choice.grid(row =3, column = 4 )
choice.current()


button1 = tk.Button(text = "CONVERT", fg = "white", bg = "#1A8246",activebackground = "#61CD8E",
                    relief = tk.RIDGE, borderwidth = 3, font = "Verdana", command = convert)
button1.grid(row = 4, column = 4, ipadx = 5, ipady = 5)

button1 = tk.Button(text = "To record press this", fg = "white", bg = "#24A158",activebackground = "#61CD8E",
                    relief = tk.RIDGE, borderwidth = 3, font = "Verdana",command = funRecord)
button1.grid(row = 2, column = 1, ipadx = 5, ipady = 5, pady = 3)

button2 = tk.Button(text = "To hear press this", fg = "white", bg = "#24A158",activebackground = "#61CD8E",
                    relief = tk.RIDGE, borderwidth = 3, font = "Verdana", command = hear)
button2.grid(row = 2, column = 7, ipadx = 5, ipady = 5, pady = 3)

textBox1 = tk.Text( width = 35, height = 15, font = "Verdana")
textBox1.grid(row = 4, column = 1)

textBox2 = tk.Text( width = 35, height = 15, font = "Verdana")
textBox2.grid(row = 4, column = 7)



window.mainloop()
