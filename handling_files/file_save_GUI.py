from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\lisha\\Desktop",
                                    defaultextension=".txt",
                                    filetypes=[("Text File", ".txt"),
                                               ("HTML File", ".html"),
                                               ("All files", ".*")])
    file_text = str(text_area.get(1.0, END))
    # or if you prefer enter text in console without text_area:
    #file_text = input("Enter some text to save: ")
    
    if file is None:
        print("No file was saved")
    else:
        file.write(file_text)
        file.close()
        text_area.delete(1.0,END)

window = Tk()

button = Button(window,
                text="Save",
                font=("Comic Sans", 15, "bold"),
                command=save_file)
button.pack()

text_area = Text(window, font=("Ink Free", 15, "bold"))
text_area.pack()

window.mainloop()