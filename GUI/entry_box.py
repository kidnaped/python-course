# entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    submitted_text = entry_box.get()
    print("You typed", submitted_text)
    entry_box.config(state=DISABLED)           # disables entry box after submit

def delete():
    entry_box.delete(0, END)

def backspace():
    entry_box.delete(len(entry_box.get())-1, END)

window = Tk()

entry_box = Entry(window,
                  font=("Comic Sans", 20, "bold"),
                  bg="grey")
entry_box.pack(side=LEFT)
#entry_box.insert(0,"Enter new text.")   # sets default text in entry box
#entry_box.config(show="*")              # replaces our text with given symbols

submit_button = Button(window,
                       text="Submit",
                       font=("Arial", 15, "bold"),
                       fg="green",
                       bg="black",
                       command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="Delete",
                       font=("Arial", 15, "bold"),
                       fg="green",
                       bg="black",
                       command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                       text="Backspace",
                       font=("Arial", 15, "bold"),
                       fg="green",
                       bg="black",
                       command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()