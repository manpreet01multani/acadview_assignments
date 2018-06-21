#1.
import tkinter as tk

r=tk.Tk()
label=tk.Label(r,text='hello world',font='size,20')
label.pack()
button=tk.Button(r,text='exit',width=20,highlightbackground='red',command='exit')
button.pack()
r.mainloop()

#2.
import tkinter as tk

r=tk.Tk()
r.title("gui app")
button=tk.Button(r,text='i will play agter sometime',width=20,command='text')
button.pack()
r.mainloop()

#3.
import tkinter as tk

def write_slogan():
    print("tkinter is easy to use!")
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()
button=tk.Button(frame,text="exit",width='20',command="exit")
button.pack(side=tk.LEFT)
label=tk.Label(frame,text='message')
label.config(text='hi ,i m here')
label.pack()
root.mainloop()

#4.

from tkinter import *
master=Tk()
Label(master,text='Name').grid(row=0)
e1=Entry(master)
e1.grid(row=0,column=1)
mainloop()
print("Name:Manpreet")
