# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "sobachiy Huy!"

#if(name[0].islower()):
#    name = name.capitalize()

name_tuple = name.partition(" ")
first_name = name_tuple[0].capitalize()
second_name = name_tuple[2].capitalize()
last_element = name[-1]

print(first_name, second_name)
print(last_element)