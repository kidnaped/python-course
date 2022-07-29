# text widget = functions like a text area, you can enter multiple lines of text

from tkinter import *
from turtle import color

def submit():
    print("Incoming transmission:",text.get("1.0",END))
    text.delete("1.0",END)

window = Tk()

text = Text(window,
            font=("Ink Free", 25, "bold"),
            fg="#2d0630",
            bg="light yellow",
            height=10,
            width=25,
            padx=20,
            pady=20)
text.pack()

button = Button(window,
                text="Submit",
                font=("Comic Sans", 15, "bold"),
                bg="#d5dfed",
                command=submit)
button.pack()

window.mainloop()