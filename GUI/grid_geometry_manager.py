# grid() = geometry manager that organizes widgets in a table-like structure in a parent window

from tkinter import *

def submit():
    bio = (first_name_entry.get(), last_name_entry.get(), email_entry.get())
    print(*bio)

window = Tk()

title_label = Label(window, text="Enter your info:").grid(row=0, column=0,columnspan=2)

first_name_label = Label(window, text="First Name: ")
first_name_entry = Entry(window)
last_name_label = Label(window, text="Last Name: ")
last_name_entry = Entry(window)
email_label = Label(window, text="Email: ")
email_entry = Entry(window)

first_name_label.grid(row=1, column=0)
first_name_entry.grid(row=1, column=1)
last_name_label.grid(row=2, column=0)
last_name_entry.grid(row=2, column=1)
email_label.grid(row=3, column=0)
email_entry.grid(row=3, column=1)

submit_btn = Button(window, text="Submit", command=submit)
submit_btn.grid(row=4, column=0, columnspan=2)

window.mainloop()
