from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 50
    download = 0
    speed = 1
    while download<GB:
        time.sleep(.05)
       
        bar["value"] += (speed/GB)*100
        download += speed
        
        percent.set(str(int((download/GB)*100))+"%")
        task.set(str(download)+"/"+str(GB)+" GB completed")
        
        window.update_idletasks()   # updates window status afret each iteration

    print("Download complete!")

window = Tk()

percent = StringVar()
task = StringVar()

bar = Progressbar(window, orient="horizontal", length=300)
bar.pack(pady=10, padx=5)

percent_label = Label(window, textvariable=percent).pack()
task_label = Label(window, textvariable=task).pack()
button = Button(window, text= "Download", command=start).pack()

window.mainloop()