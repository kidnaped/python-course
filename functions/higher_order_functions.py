# Higher Order Function = a function that either:
#                         1. accepts a function as an argument
#                         or
#                         2. returns a function
#                         (In Python functions are also treated as objects)

# example of 1
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func(input("Enter what you're gotta say: "))
    print(text)

hello(loud)             # we accept a loud() or quiet() func as arguments
hello(quiet)

# example of 2
def divisor(x):         # its high order function, cause we returning dividend
    def dividend(y):
        return y/x
    return dividend

divide = divisor(5)     # we passing x=5 and skipping dividend(), but return dividend and assigning it to a variable
print(divide(10))       # so divide = dividend, where x=5, and assign y=10, then return y/x
