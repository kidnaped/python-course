# label = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file='logo.png')

label = Label(window, 
              text="Hello World", 
              font=("Arial", 40, "bold"), 
              fg="#2d0630",         # foreground color
              bg="#8f4f0a",         # background color
              relief=RAISED,        # border style can be SUNKEN etc
              bd=10,                # border width
              padx=20,              # padding text from borders
              pady=15,
              image=photo,          # adds an image from PhotoImage obj
              compound="bottom")    # places image in desired location
                    

label.pack()    # places our label in the middle upper position of a window by default
# anothre way to do this, but with place of our choise
#label.place(x=0, y=0)


window.mainloop()