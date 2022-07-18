import os
import shutil

file_path = "D:\\Documents\\sandbox\\not_empty_folder"

try:
    #os.remove(file_path)    # removes file, but NOT the folder
    #os.rmdir(file_path)      # removes ONLY empty folder
    shutil.rmtree(file_path)    # removes ANY folders and its containts
except FileNotFoundError as e:
    print(e)
    print("There is no file to delete.")
except PermissionError as e:
    print(e)
    print("You have not enough rights to do that!")
except OSError as e:
    print(e)
    print("Wrong function for deleting that item!")
else:
    print(file_path,"was deleted!")