from tkinter import *

def doSomething(event):
    print("Mouse coordinates", str(event.x), str(event.y))


window = Tk()

#window.bind("<Button-1>", doSomething)  # left mouse click
#window.bind("<Button-2>", doSomething)  # middle mouse click
#window.bind("<Button-3>", doSomething)  # right mouse click
#window.bind("<ButtonRelease>", doSomething) # start event on releasing mouse button
#window.bind("<Enter>", doSomething)     # starts event when mouse entering window
#window.bind("<Leave>", doSomething)     # starts event when mouse leaves window
window.bind("<Motion>", doSomething)    # starts event when moving the cursor

window.mainloop()