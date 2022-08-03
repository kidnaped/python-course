# canvas = widget, that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
#canvas.create_line(0,0, 500,500, fill="purple",width=20)
#canvas.create_line(0,500, 500,0, fill="red",width=20)
#canvas.create_rectangle(75,160, 200,260, fill="green", outline="yellow", width=10)
#points = [137,255, 75,350, 200,350]
#canvas.create_polygon(points, fill="brown", outline="orange", width=5)
#canvas.create_arc(70,40, 200,170, fill="pink",style=PIESLICE, start=225)
canvas.create_arc(0,0, 500,500, fill="red", extent=180, width=10)
canvas.create_arc(0,0, 500,500, fill="white", extent=180, start=180, width=10)
canvas.create_oval(190,190, 310,310, fill="white", width=10)

canvas.pack()

window.mainloop()