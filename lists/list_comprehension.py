# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda func, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if conditional]
#                      list = [expression if/else for item in iterable]

# usual way to create a list
#squares = []                # create an empty list
#for i in range(1, 21):      # create a for loop
#    squares.append(i*i)     # define each loop iteration do
#print(squares)

# simple list comprehension way
#squares = [i * i for i in range(1,21)]
#print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

# one way to filter students
# passed_students = list(filter(lambda x: x >= 60, students))

# comprehension way
# passed_students = [item for item in students if item >= 60]

# fancy comprehension way
# we replace items in list which don't meet conditions with "FAILED" str
passed_students = [item if item >= 60 else "FAILED" for item in students]

print(passed_students)
