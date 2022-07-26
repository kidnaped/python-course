# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemin threads can't normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for", count, "seconds")

# programm will work until killed, despite we coplete program in main thread
# to avoid this - we must add daemon=True parameter in our thread
x = threading.Thread(target=timer, daemon=True)

# or
x.setDaemon(True)
x.start()

answer = input("Do you want to exit? ")