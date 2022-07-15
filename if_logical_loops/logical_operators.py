# logical operators (and, or, not) used to chech if 2 or more conditional statements are true

temp = float(input("What is the temperature outside?: "))

# if temp >= 0 and temp <= 30:
#    print("The temperature is qute good!")
#   print("Go outside!")
# elif temp < 0 or temp > 30:
#    print("The weather is not good for you!")
#    print("Stay inside!")

# explaining NOT operator
if not(temp >= 0 and temp <= 30):
    print("The weather is not good for you!")
    print("Stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is qute good!")
    print("Go outside!")
