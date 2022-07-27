# buttons = you click - they do

from tkinter import *

count = 0
def click():
    global count
    count += 1
    print("You clicked Me", count, "times!")

window = Tk()

button_image = PhotoImage(file="ext128.png")

button = Button(window,
                text="Click Me!",
                font=("Comic Sans", 30, "bold"),
                fg="#2d0630",
                bg="#8f4f0a",
                activeforeground="#2d0630",     #change color when clicked
                activebackground="#8f4f0a",
                command=click,                  # function without () is called callback
                state=ACTIVE,                   # enevles or disables clickin on the button
                image=button_image,
                compound="left")

button.pack()

window.mainloop()