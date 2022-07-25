# ****************************  
# if __name__ == "__main__"
#*****************************
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules
#
# Python interpreter sets "special variables", one of wich is __name__
# then Python will execute the code found within __main__ 
# if it's the initial module being run

# explainings about __name__

'''import test_module

print(__name__)             # will print __main__ cause executes in body of this module
print(test_module.__name__) # will print name of module being imported, cause you know... it's imported
'''
if __name__ == "__main__":
    print ("running this module directly")
else:
    print("running module as imported")