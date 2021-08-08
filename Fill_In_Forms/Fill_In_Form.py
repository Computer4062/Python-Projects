import tkinter as tk
from tkinter import messagebox

root = tk.Tk ()
canvas1 = tk.Canvas(root,width=300,height=300)
canvas1.pack ()

def calc () :
    name = name_Entry.get ()
    age = age_entry.get()
    SecondName = SecondName_entry.get()

name_entry = tk.Entry(root,text = "name")
canvas1.create_window(215,75,window= name_entry)
name_label = tk.Label(root, text = 'Enter your name here:')
canvas1.create_window(95,75,window= name_label)

age_entry = tk.Entry(root,text="age")
canvas1.create_window(215,105,window=age_entry)
age_label = tk.Label(root,text='Enter your age here:')
canvas1.create_window(95,105,window= age_label)

SecondName_entry = tk.Entry(root,text='SecondName')
canvas1.create_window(215,135,window=SecondName_entry)
SecondName_label = tk.Label(root,text='Enrter  your second name here :')
canvas1.create_window(95,135,window=SecondName_label)

root.mainloop ()




