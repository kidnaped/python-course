# str.format() = optional method that gives users
#                more control when displaying output

animal = "cow"      #globals
item = "moon"

#print("The", animal, "jumped over the", item)
#print("The {0} jumped over the {1}".format(animal, item)) # positional argument, indexes in {} can be switched places
#print("The {animal} jumped over the {item}".format(animal="cow", item="rainbow")) #another way, using local vars

#print(f"The {animal} jumped over the {item}") #the most efficient way

#MORE ELEGANT METHOD
#text = "The {} jumped over the {}"

#print(text.format(animal, item))

# important features
'''print("Hello {}".format(animal))
print("Hello {:10}, I've been waiting.".format(animal))  # adds 10 spaces after variable
print("Hello {:>10}, I've been waiting.".format(animal)) # positions var right after spaces
print("Hello {:<10}, I've been waiting.".format(animal)) # positions var left of the spaces
print("Hello {:^10}, I've been waiting.".format(animal)) # positions var in the middle of spaces'''

# .format() works with numbers too
num = 1000

print("The number is {:.2f}.".format(num)) # displays num, but with 2 digits after "."
print("The number is {:,}.".format(num))   # adds "," in thousands
print("The number is {:b}." .format(num))   #binary interpretation
print("The number is {:o}.".format(num))    #octo number
print("The number is {:x}.".format(num))    #hexodecimal number
print("The number is {:e}.".format(num))    #scientific notation