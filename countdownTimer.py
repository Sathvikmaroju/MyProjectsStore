from tkinter import *
from tkinter import ttk, font
import time
import datetime


global endTime

def quit(*args):
    root.destroy()

def cant_wait():
    time_left = endTime - datetime.datetime.now()
    time_left -= datetime.timedelta(microseconds=time_left.microseconds)
    txt.set(time_left)
    root.after(1000,clock_time)

root = Tk()
root.attributes("-fullscreen",False)
root.minsize(900,200)
root.configure(background='black')
root.bind("x",quit)
root.after(1000,cant_wait)

endTime = datetime.datetime(2222,1,1,0,0) # year - month - date - hour - min
#endTime is the time when it goes kaboom!
fnt = font.Font(family='Helvetica',size=60,weight='bold')
txt = StringVar()
lbl = ttk.Label(root,textvariable=txt,font=fnt,foreground='white',background='black')
lbl.place(relx=0.5,rely=0.5,anchor='center')
root.mainloop()