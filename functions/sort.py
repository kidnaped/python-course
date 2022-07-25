# sort() method = used with lists
# sorted() function = used with iterables

#students = ["Solevoy", "Podbitiy", "Kumar", "Podpivasnik", "Derevo"]

'''students.sort(reverse=True) # () empty if we want ascending order, reverse=True if descending
for i in students:
    print(i)'''

'''sorted_students = sorted(students, reverse=True)
for i in sorted_students:
    print(i)'''

# sort() method with list of tuples, where we sort by age, last name and grade
'''students =[("Solevoy", "F", 60),
           ("Podbitiy", "A", 33),
           ("Kumar", "D", 36),
           ("Podpivasnik", "B", 20),
           ("Derevo", "C", 78)]

grade = lambda grades: grades[1]
last_name = lambda last_names: last_names[0]
age = lambda ages: ages[2]

students.sort(key= grade)
for i in students:
    print(*i)
print("-----------------------------------")'''

# sorted() func but with tuple of tuples
students = (("Solevoy", "F", 60),
            ("Podbitiy", "A", 33),
            ("Kumar", "D", 36),
            ("Podpivasnik", "B", 20),
            ("Derevo", "C", 78))

grade = lambda grades: grades[1]
last_name = lambda last_names: last_names[0]
age = lambda ages: ages[2]

students_sorted = sorted(students, key= age)
for i in students_sorted:
    print(*i)
    print("-----------------------------------")