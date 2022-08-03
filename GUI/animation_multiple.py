from tkinter import *
from anim_ball_calss import *
import time

WIDTH = 500     # defining constants with upper letters
HEIGHT = 500

running = True

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0,0, 100, 2,5, "blue")
tennis_ball = Ball(canvas, 0,0, 50, 3.5,6, "yellow")
basket_ball = Ball(canvas, 0,0, 70, 7,4, "orange")

while running:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()