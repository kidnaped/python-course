from tkinter import *
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\lisha\\Desktop",
                                           title="Chose a File",
                                           filetypes=(("Text Files", "*.txt"),
                                           ("all files","*.*")))
    if file_path == "":
        print("No file selected")
    else:
        file = open(file_path, 'r')
        print(file.read())
        file.close()

window = Tk()

button = Button(window,
                text="Open a File",
                font=("Comic Sans", 15, "bold"),
                bg="#d5dfed",
                command=open_file)
button.pack()

window.mainloop()