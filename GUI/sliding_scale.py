from tkinter import *

def submit():
    print("Temperature is:", scale.get(), "C")

window = Tk()

# place label before scale
hot_image = PhotoImage(file="fire.png")
hot_label = Label(image=hot_image)
hot_label.pack()

scale = Scale(window,
              from_=200, 
              to=0,
              length=600,
              orient=VERTICAL,      # or HORISONTAL
              font=("Consolas", 15),
              tickinterval=10,      # numeric indicators for value
              showvalue=0,          # hides or shows current value
              resolution=5,
              troughcolor="grey",
              fg="yellow",
              bg="black",
              
              )

scale.set(((scale["from"]-scale["to"])/2)+scale["to"])  # set current value of scale
scale.pack()

# place label after scale and before button
cold_image = PhotoImage(file="snow.png")
cold_label = Label(image=cold_image)
cold_label.pack()

button = Button(window,
                text="Submit",
                command=submit,
                font=("Consolas", 12, "bold"))
button.pack()

window.mainloop()