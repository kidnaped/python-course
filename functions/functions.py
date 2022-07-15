# function = a block of code, which is executed only when its called

#def hello(name):
#    print("Hello " + name)
#    print("Have a nice day!")

#hello("BRo")

# OR we can do it better
#here we straigt asking for input in defenition of function

#def hello(name = input("Enter your name: ")):      
#    print("Hello " + name)
#    print("Have a nice day!")

#hello()

# OR another way
# here we create var asking for an input and paste it to our fuction as argument
def hello(firts_name, last_name, age):
    print("Hello", firts_name, last_name)
    print("You are", age, "years old.")
    print("Have a nice day!")

my_first_name = input("Enter your first name: ")
my_last_name = input("Enter your last name: ")
my_age = input("Enter your age: ")
hello(my_first_name, my_last_name, my_age)
