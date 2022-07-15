try:
    with open("test.tx") as file:      #or use full path to it, if it's not in project dir
        print(file.read())              #"with open" closes file automatically, but not handling any exceptions
except FileNotFoundError:
    print("Incorrect file name or path!")
except Exception:
    print("Smth went wrong!")

#print(file.closed)
