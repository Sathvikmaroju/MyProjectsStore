import smtplib
from tkinter import *

def send():
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(senderEmail_entry.get(), senderEmail_password_entry.get())
    s.sendmail(senderEmail_entry.get(),receiverEmail_entry,message)
    s.quit()

root = Tk()

root.geometry("733x434")
root.minsize(434, 373)
root.title("Send Email with python")

senderEmail_value, senderEmail_password_value = StringVar(), StringVar()
receiverEmail_value, message_value = StringVar(), StringVar()

frame_senderEmail = Frame(root, borderwidth=3)
frame_senderEmail.pack(side=TOP,anchor="nw")
from_email = Label(frame_senderEmail, text="From")
from_email.grid()
senderEmail_entry = Entry(frame_senderEmail, textvariable = senderEmail_value)
senderEmail_entry.grid(row=0, column=1)

frame_senderEmail_password = Frame(root, borderwidth=3)
frame_senderEmail_password.pack(anchor="nw")
from_email_password = Label(frame_senderEmail_password, text="Password")
from_email_password.grid()
senderEmail_password_entry = Entry(frame_senderEmail_password, textvariable = senderEmail_password_value)
senderEmail_password_entry.grid(row=0, column=1)

frame_receiverEmail = Frame(root, borderwidth=3)
frame_receiverEmail.pack(anchor='nw')
to_email = Label(frame_receiverEmail, text="To")
to_email.grid()
receiverEmail_entry = Entry(frame_receiverEmail, textvariable = receiverEmail_value)
receiverEmail_entry.grid(row=0, column=1)

frame_message = Frame(root, borderwidth=3,relief=SUNKEN)
frame_message.pack(anchor='nw')
message = Label(frame_message, text="Message")
message.grid()
message_entry = Entry(frame_message, textvariable=message_value)
message_entry.grid(row=0, column=1)

frame_button = Frame(root, borderwidth=3, relief=GROOVE)
frame_button.pack(side=BOTTOM,anchor="se")
send_button = Button(frame_button, fg="black", text=" Send  ",command=send)
send_button.pack()

root.mainloop()