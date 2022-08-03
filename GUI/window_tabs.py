from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) # widget manages a collection of windows/displays

tab_1 = Frame(notebook) #new frame for tab_1
tab_2 = Frame(notebook)

notebook.add(tab_1, text="Tab 1")
notebook.add(tab_2, text="Tab 2")
notebook.pack(expand=True, fill="both")  # expand = expand to fill space unused by other widgets
                                         # fill = fill space on x and y axis 
Label(tab_1, 
      text="This is Tab 1", 
      font=("Comic Sans", 20, "bold"),
      bg="#303030",
      fg="#83d2e0",
      width=25, height=12).pack()

Label(tab_2, 
      text="This is Tab 2", 
      font=("Comic Sans", 20, "bold"),
      bg="#dbd6b0",
      fg="#24264a",
      width=25, height=12).pack()

window.mainloop()