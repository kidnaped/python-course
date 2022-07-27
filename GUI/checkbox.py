from tkinter import *

def display():
    if x.get():
        print("You agreed to something")
    else:
        print("You did not agree :'(")

window = Tk()

x = BooleanVar()

logo = PhotoImage(file="ext128.png")
check_box = Checkbutton(window,
                        text="I agree to something",
                        variable=x,     # variable that stores some value
                        onvalue=True,      # returns given value to var when checkbox on
                        offvalue=False,     # returns given value to var when checkbox off
                        command=display,
                        font=("Arial", 20, "bold"),
                        fg="green",
                        bg="black",
                        activeforeground="green",
                        activebackground="black",
                        padx=20,
                        pady=15,
                        image=logo,
                        compound="left")
check_box.pack(side=LEFT)


window.mainloop()