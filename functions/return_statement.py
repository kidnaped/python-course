# return statement =    functions send Python values/objects back to the caller.
#                       These values/objects are known as the function's return value

def multiply(num1, num2):
    #result = num1 * num2
    # we can do it straight
    return num1 * num2

x = int(input("X = "))
y = int(input("Y = "))
z = multiply(x,y)

print(z)