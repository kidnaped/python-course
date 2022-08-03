from tkinter import *
from time import *

def update():
    time_str = strftime("%H:%M:%S")
    time_label.config(text=time_str)     # adds text with current time to a time label

    day_str = strftime("%A")
    day_label.config(text=day_str)       # adds text with current weekday to a day label

    date_str = strftime("%d %B %Y")      # adds text with current date to a date label
    date_label.config(text=date_str) 

    window.after(1000, update)           # rerun update function after 1000ms

running = True

window = Tk()

# label for time
time_label = Label(window, font=("Arial", 50, "bold"), fg="green", bg="black")
time_label.pack()

# label for day of the week
day_label = Label(window, font=("Ink Free", 30, "bold"))
day_label.pack()

# label for a date
date_label = Label(window, font=("Ink Free", 25, "bold"))
date_label.pack()

update()

window.mainloop()