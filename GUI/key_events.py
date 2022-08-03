from cProfile import label
from tkinter import *

def doSomething(event):
    #print("You pressed", event.keysym)     #keysym = simulates and shows pressed keyboard button
    key_label.config(text=event.keysym)
    
window = Tk()

window.bind("<Key>", doSomething)

key_label = Label(window, font=("Helvetica", 50))
key_label.pack()

window.mainloop()