from tkinter import *

def open_file():
    print("File has been opened!")

def save_file():
    print("File has been saved!")

def cut():
    print("Text cut")

def copy():
    print("Text copied")

def paste():
    print("Text pasted")

window = Tk()

exit_image = PhotoImage(file="D:\\Documents\\Git\\python-course\\GUI\\fire.png")

menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0, font=("MV Boli", 10))
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit, image=exit_image, compound="left")

edit_menu = Menu(menubar, tearoff=0, font=("MV Boli", 10))
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

window.mainloop()