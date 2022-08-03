from tkinter import *

def new_window():
    nw = Tk() # TopLevel() = new window "on top" of other windows, 
                    # linked to a "bottom" window, useful for temporary windows.
                    # Tk() = new independent window, useful for login windows etc.
    old_window.destroy()

old_window = Tk()

Button(old_window, 
       text="Create a New Window", 
       font=("Comic Sans", 15, "bold"), 
       command=new_window).pack()

old_window.mainloop()