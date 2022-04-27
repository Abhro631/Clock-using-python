from tkinter import *
from tkinter.ttk import *
 
from time import strftime
 
root = Tk()
root.title("Clock")
 
def time():
    str = strftime('%H:%M:%S %p')
    label.config(text=str)
    label.after(1000, time)
 
label = Label(root, font=("ds-digital", 150), background = "black", foreground = "green")
label.pack(anchor='center')
time()
 
mainloop()