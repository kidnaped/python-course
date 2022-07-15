# *args = parameter that will pack all arguments into tuple
#         useful so that a function can accept a varying amount of arguments

# we get an error if give >2 arguments to this function
#def add(num1,num2):
#    sum = num1 + num2
#    return sum
#print(add(1,2,3))

# how it solved with *args parameter of function
def add(*args):     # args can be renamed as you like, "*" is IMPORTANT berore parameter name
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(12,13,14,15,16))