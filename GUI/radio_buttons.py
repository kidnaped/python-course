# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

icons = ["Smile", "Smile with Horns", "Smiling Dock"]

def choice():
    
    if x.get() == icons.index(icons[x.get()]):  # compare int value from chosen button with int value from list element
        print(f"You choose {icons[x.get()]}")   # print 

window = Tk()

x = IntVar()

smile_image = PhotoImage(file="ase64.png")
horns_image = PhotoImage(file="ext64.png")
dock_image = PhotoImage(file="doc64.png")

images_list = [smile_image, horns_image, dock_image]

for index in range(len(icons)):
    radiobutton = Radiobutton(window,
                              text=icons[index], # adds tex to radiobuttuns
                              font=("Impact", 30, "bold"),
                              padx=15,
                              pady=10,
                              indicatoron=0,     # eliminate circle indicator and turn it to a pushbutton
                              width=400,         # sets width of radiobuttons
                              image=images_list[index],
                              compound="left",
                              variable=x,        # groups rdbuttons together if they share same variable
                              value=index,       # assigns each rdbutton a different value
                              command=choice)
    radiobutton.pack(anchor=W)      # anchors radiobuttons in the west part of window


window.mainloop()