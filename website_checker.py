import urllib.request
import tkinter as tk

def check_web():
    link = e.get()
    a = urllib.request.urlopen(link).getcode()
    if a == 200:
        label = tk.Label(frame, text=link + " is up")
        label.pack()
    else:
        label = tk.Label(root, text=link + " is down")
        label.pack()

root = tk.Tk()
root.title("Website Checker")
e = tk.Entry(root, width=54, bg="lightblue")
e.pack()
canvas = tk.Canvas(root, height=230, width=320, bg='#263D42')
canvas.pack()
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
checkLink = tk.Button(root, text="Check", padx=9, pady=6, fg="white", bg='#263D42', command=check_web)
checkLink.pack()
root.mainloop()