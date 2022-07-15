import imp
import time
# for loop =    a statement that will execute its block of code
#               a limited amount of time
#
#               while loop = unlimited
#               for loop = limited

#for i in range(10):
#    print(i+1)

#for i in range(50,100+1,2): #the third argument (2) is considered as step for count, like in slicing and indexting
#   print(i)

#for i in "Sutulaya Sobaka":
#    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("BOOM!")
