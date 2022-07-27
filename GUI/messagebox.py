from tkinter import *
from tkinter import messagebox  # imports messagebox library

def click():
    #messagebox.showinfo(title="Message:", message="You entering a dark space!")
    #messagebox.showwarning(title="WARNING", message="You playing with fire, bro!")
    #messagebox.showerror(title="ERROR:", message="I CAUGHT YOU!")

    '''if messagebox.askokcancel(title="Question", message="Dou you want or not?"):
        print("You want and not scared")
    else:
        print("You are a little pussy boy")'''

    '''if messagebox.askretrycancel(title="RETRY", message="Dou you want to retry something?"):
        print("A brave one, aren't you?")
    else:
        print("You are a bitchy little pussy")'''

    '''if messagebox.askyesno(title="DOSTOEVSKY", message="Do you have a RIGHT?"):
        print("You HAVE a RIGHT!")
    else:
        print("You are a trembling thing!")'''

    '''answer = messagebox.askquestion(title="My question is:", message="Are you mad or something?")
    if answer == "yes":
        print("You need immediate treatment!")
    else:
        print("You are OK")'''

    answer = messagebox.askyesnocancel(title="DOSTOEVSKY", message="Did you kill an old lady?!", icon="error")
    if answer:
        print("You are going to GULAG!")
    elif answer == None:
        print("Not this time!")
    else:
        print("Sorry, sir, you are free to go")

window = Tk()

button = Button(window, 
                text="Click me!",
                font=("Constantia", 20, "bold"),
                width=15,
                bg="#d5dfed",
                command=click)
button.pack()

window.mainloop()