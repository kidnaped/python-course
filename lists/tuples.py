# tuple =   collection which is ordered and unchangable
#           used to group together related data

student = ("Bratishka", 27, "bigender")

#print(student.count("Bratishka"))
#print(student.index("bigender"))

for x in student:
    print(x, end = " ")

if "Bratishka" in student:
    print("\nHere you are!")