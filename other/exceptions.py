# exceptions = events detected duting execution that inerrupts the flow of a program

# basic form of exception handling
# under try code we place any code, concidering dangerous that might cause an exception
try:            
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:      # "as e" copys text of exception into a variable called "e"
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("You can't use letters!")
# deals with ALL exceptions, Not a good practice, cause not showing details
# better practice to some specific exceptions that may occur
except Exception as e:
    print(e)           
    print("Smth went wrong!")
else:       # execute code only if there's no exceptions
    print(result)
finally:    # execute code whether or not there are exceptions
    print("Tis will always execute.")
