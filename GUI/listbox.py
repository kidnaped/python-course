# listbox = list of selectable text items within it;s own container

from tkinter import *

def submit():
    
    food = []

    if listbox.curselection() == ():            # here empty () = nothing was selected
        print("You haven't ordered anything!")
    else:
        for index in listbox.curselection():
            food.insert(index, listbox.get(index))
    
        print("You ordered:")
    
        for index in food:
            print(index)

# adds position to a menu, clears input space and menu's height
def add():
    
    if entry_box.get() == "":
        print("You can not add empty space!")
    else:
        listbox.insert(listbox.size(), entry_box.get())
        entry_box.delete(0,END)
    
    listbox.config(height=listbox.size())

# deletes chosen positions in menu and ajust its height
def delete():
    
    for index in reversed(listbox.curselection()):  # revesed (from last to first) allow to avoid index cahnges after first item deletion
        listbox.delete(index)
    
    listbox.config(height=listbox.size())

window = Tk()

# create and customize lisbox
listbox = Listbox(window,
                  bg="#bbd6b4",
                  font=("Constantia", 20, "bold"),
                  width=13,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Pinapple")
listbox.insert(2, "Yoghurt")
listbox.insert(3, "Ice Cream")
listbox.insert(4, "Banana")
listbox.insert(5, "Pile of Garbage")

listbox.config(height=listbox.size())   # define height of lisbox depending of it containts

# create entrybox
entry_box = Entry(window,
                  font=("Comic Sans", 20, "bold"),
                  width=14)
entry_box.pack()

# create some buttons and define their behaviour
submit_button = Button(window,
                       text="Submit",
                       font=("Comic Sans", 15, "bold"),
                       width=15,
                       bg="#d5dfed",
                       command=submit)
submit_button.pack()

add_button = Button(window,
                       text="Add",
                       font=("Comic Sans", 15, "bold"),
                       width=15,
                       bg="#d5dfed",
                       command=add)
add_button.pack()

delete_button = Button(window,
                       text="Delete",
                       font=("Comic Sans", 15, "bold"),
                       width=15,
                       bg="#d5dfed",
                       command=delete)
delete_button.pack()

window.mainloop()