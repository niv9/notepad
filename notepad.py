# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:14:57 2024

@author: MS Surface Laptop
"""

from tkinter import*
root=Tk()
from tkinter import messagebox
import os
from PIL import ImageTk,Image
from tkinter import filedialog
root.minsize(650,650)
root.maxsize(650,650)
root.title("MINI NOTEPAD")
root.configure(bg="yellow")

open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))

l1=Label(root,text="file name")
l1.place(relx=0.28,rely=0.03,anchor=CENTER)

e1=Entry(root)
e1.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text=Text(root,height=40,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0,END)
    e1.delete(0,END)
    text_file = filedialog.askopenfilename(title = "open text file",filetypes=(("text files","*.html"),))
    print(text_file)
    name=os.path.basename(text_file)
    formatted_name= name.split(".")[0]
    e1.insert(END,formatted_name)
    root.title(formatted_name)
    text_file = open(name,"r")
    paragraph=text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()
    
def save ():
   input_name=e1.get()
   file=open(input_name+".html","w")
   data=my_text.get("1.0",END)
   file.write(data)
   e1.delete(0,END)
   my_text.delete(1.0,END)
   messagebox.showinfo("update","the file is saved")
   
def close():
    root.destroy()

button1=Button(root,image=open_img,command=openFile)
button1.place(relx=0.05,rely=0.03,anchor=CENTER)
button2=Button(root,image=save_img, command=save)
button2.place(relx=0.11,rely=0.03,anchor=CENTER)
button3=Button(root,image=exit_img,command=close)
button3.place(relx=0.17,rely=0.03,anchor=CENTER)

root.mainloop()
