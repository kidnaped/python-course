# nested function calls =   function calls inside other function calls
#                           innermost function calls are resolved first
#                           returned value is used as argument for the next outer function

#num = input("Enter a whole positive number: ")
#num = float(num)    # makes it float
#num = abs(num)      # return absolut value (positives any number)
#num = round(num)    # rounds the number

#num = round(abs(float(num)))    # quicker and lighter version NESTED FUNCTION CALL
#print(num)

# OR we just can go with that
print(round(abs(float(input("Type a whole positive number: ")))))