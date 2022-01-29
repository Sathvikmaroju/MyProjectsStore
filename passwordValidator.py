from tkinter import *
from functools import partial

def validatepassword():
    if ep.get()==cp.get():
        Label(root,text='Password Matches').grid(row=5,column=0)
    else:
        Label(root,text='Password not match').grid(row=5,column=0)

root = Tk()
root.geometry('280x95')
root.title('Password Validation')

label1 = Label(root,text='Enter password').grid(row=0,column=0)
ep = StringVar()
passwordEntry = Entry(root,textvariable=ep,show='*').grid(row=0,column=1)

label2 = Label(root,text='Confirm password').grid(row=1,column=0)
cp=StringVar()
confirmPassword = Entry(root,textvariable=cp,show='*').grid(row=1,column=1)

checkbtn = Button(root,text='Check',command=validatepassword).grid(row=4,column=0)

root.mainloop()