# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

# we get an error if give >2 arguments to this function
#def hello(first, last):
#    print("Hello", first, last)
#hello (first= "Sobachya", middle= "Tupaya", last= "Zhopa")

# solving the problem
def hello(**kwargs):
    #print("Hello", kwargs['first'], kwargs['last'])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")
    
hello(first="Sobachya", middle="Tupaya", last="Zalupa")