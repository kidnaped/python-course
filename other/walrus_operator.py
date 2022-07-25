# walrus operator := assignment expression
# assigns values to variables and use them as part of a larger expression

"""happy = True
#print(happy)

print(happy := False)"""

'''foods = list()
while True:
    food = input("What food do you like: ").lower()
    if food == "quit":
        break
    foods.append(food)
print(*foods)'''

# the same program, but using the walrus operator

foods = list()
while str(food := input("What food do you like: ").lower()) != "quit":
    foods.append(food)
print(*foods)