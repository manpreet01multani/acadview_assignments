#1.
from tkinter import *
r=Tk()
d={"Meet":789,"jeet":456,"heer":786,"reet":234,"geet":987,"geen":675,"reet":345}
label=Label(r,text="Name",font='size,10')
label.pack(side="bottom")
label=Label(r,text="phone number")
label.pack(side="top")

def handleList(event):
    label3=mn.get(ACTIVE)
    print(label3)
    ph=d.get(label3)
    global label1,label2
    label1.config(text=label3)
    label2.config(text=ph)

mn=Listbox(r)
mn.config(selectmode=EXTENDED)
scrollbar=Scrollbar(r)
scrollbar.config(command=mn.yview)
mn.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT,fill=Y)
mn.pack(side=LEFT,expand=YES,fill=BOTH)

mn.bind('<Double-1>',handleList)
for k,v in d.items():
    mn.insert('end',k)
r.mainloop()
