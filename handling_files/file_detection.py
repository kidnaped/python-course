import os

file_path = "C:\\Users\\lisha\\Desktop\\test_folder"    # \\ is added to path to exclude escape sequences for a str like \t, \n etc

if os.path.exists(file_path):       # checks if the location exists in OS
    print("This location exists")
    if os.path.isfile(file_path):
        print("That is a file!")
    elif os.path.isdir(file_path):
        print("Thay is a Folder!")
else:
    print("This location doestn't exists")
