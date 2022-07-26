#********************************
# Python multiprocessing
#********************************
# Multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
# Multiprocessing = better for CPU bound tasks (heavy CPU usage)
# Multithreading = better for IO bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count <= num:
        count += 1

def main():
    
    print(cpu_count())

    a = Process(target=counter, args=(250000000,))     # create process  
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    a.start()                                           # start process
    b.start()
    c.start()
    d.start()

    a.join()                                            # syncronize process with main process
    b.join()
    c.join()
    d.join()

    print("Finished in", time.perf_counter(), "seconds")


if __name__ == "__main__":
    main()