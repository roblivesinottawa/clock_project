from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime



def quit(*args):
    root.destroy()

def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%Y-%m-%d %H:%M:%S"))
    txt.set(time)
    
    
    root.after(1000, clock_time)


root = Tk()
root.attributes("-fullscreen", False)
root.configure(background="black")
root.bind("x", quit)
root.after(1000, clock_time)


fnt = font.Font(family="Sans-Serif", size=80, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="grey", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()
