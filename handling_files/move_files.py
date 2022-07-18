import os

source = "move_file.txt"    # also we can move folders
destination = "D:\\Downloads\\test_folder\\move_file.txt"

try:
    if os.path.exists(destination):
        print("There is a file there.")
    else:
        os.replace(source, destination)
        print(source, "was moved.")
except FileNotFoundError as e:
    print(e)
    print(source, "was not found.")
