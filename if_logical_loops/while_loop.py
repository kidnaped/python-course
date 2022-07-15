# while loop =  a statement that will execute it's block of code
#               as long as it's condition remains true

# example of infinite loop
#while 1==1:
#    print("Help! I'm going crazy!")

#name = ""
#while len(name) == 0:
#    name = input("Enter you name: ")

#print("Hello " + name)

# another way - define name as None and add in loop NOT. i.e. while there is NO NAME it keeps asking for NAME
name = None
while not name:
    name = input("What is you name: ")

print("Hello " + name)


