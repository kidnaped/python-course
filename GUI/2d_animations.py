from tkinter import *
import time

WIDTH = 500     # defining constants with upper letters
HEIGHT = 500

running = True

x_velocity = 1.5
y_velocity = 4

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

photo_background = PhotoImage(file="forest.png")
my_bg = canvas.create_image(0,0, image=photo_background, anchor=NW)

photo_image = PhotoImage(file="fire.png")
my_image = canvas.create_image(0,0, image=photo_image, anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while running:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if (coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0):
        x_velocity = -x_velocity
    if (coordinates[1] >= (HEIGHT-image_height) or coordinates[1] < 0):
        y_velocity = -y_velocity
    canvas.move(my_image, x_velocity, y_velocity)
    window.update()
    time.sleep(0.01)

window.mainloop()