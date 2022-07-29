from tkinter import *
from tkinter import colorchooser    # submodule

def chose_color():

    color = colorchooser.askcolor()
    window.config(bg=color[1])
    
    print("You chose", color[1], "color")

    # more effective way
    #print("You chose", colorchooser.askcolor()[1], "color")
    #window.config(bg=colorchooser.askcolor()[1])

window = Tk()
window.geometry("420x420")

button = Button(window,
                text="Chose your color",
                font=("Comic Sans", 15, "bold"),
                width=15,
                bg="#d5dfed",
                command=chose_color)
button.pack()

window.mainloop()

