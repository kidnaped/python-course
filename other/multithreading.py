# thread - a flow of execution. Like a separate order of instructions.
#                               However each thread takes a turn running to achieve concurrency
#                               GIL = (global interpreter lock)
#                               allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of its time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time

def brush_teeth():
    time.sleep(3)
    print("You brushed teeth")

def get_dressed():
    time.sleep(2)
    print("You dressed")

def go_to_kindergarden():
    time.sleep(5)
    print("You went to kindergarden")

#brush_teeth()           # executes in order one by one
#get_dressed()
#go_to_kindergarden()

# now we create 3 different threads for our functions to execute concurrently
x = threading.Thread(target=brush_teeth, args=())
x.start()

y = threading.Thread(target=get_dressed, args=())
y.start()

z = threading.Thread(target=go_to_kindergarden, args=())
z.start()

x.join()        # telling our main thread to wait until other thread copletes
y.join()        # and only then execute its set of instructions
z.join()

print(threading.active_count()) # shows number of threads executing
print(threading.enumerate())    # shows threads
print(time.perf_counter())      # shows howlong it takes our main thread to finish its set of instructions