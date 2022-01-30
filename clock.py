from tkinter import *
from tkinter import ttk, font
import time
import datetime

def quit(*args):
    root.destroy()

def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%Y-%m-%d  %H:%M:%S")) # date and time
    #time = (time.strftime("%H:%M:%S")) # time
    txt.set(time)
    root.after(1000,clock_time)

root= Tk()
root.title("Time")
root.attributes("-fullscreen",False)
root.minsize(900,200)
root.configure(background='black')
root.bind("x",quit)
root.after(1000,clock_time)

fnt = font.Font(family='Helvetica',size=60,weight='bold')
txt=StringVar()
lbl=ttk.Label(root,textvariable=txt,font=fnt,foreground='white',background='black')
lbl.place(relx=0.5,rely=0.5,anchor='center')
root.mainloop()