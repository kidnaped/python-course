# GUI = graphical user interface
# We would used TKinter module frop Python library

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

from tkinter import *   # here we import everything from tkinter module

window = Tk()   # instanciate an instance of a window, but not display it
window.geometry("500x500")
window.title("The King of Hills")

icon = PhotoImage(file="logo.png")   # convert our logo.png (NOT recognize JPG) file into a PhotoImage file
window.iconphoto(True, icon)         # sets our logo,png as a icon for a window
#window.config(background="Dark blue")# set background color with words
window.config(background="#0f002e")   # set background color with hex number

window.mainloop()   # display our window, listen for events


