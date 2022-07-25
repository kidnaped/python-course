# filter() = creates a collection of elements from an iterable for which a fuc returns true
# filer(func, iterable)

friends = [("Sasha", 19), 
           ("Dima", 18),
           ("Dusya", 17),
           ("DAnila", 20),
           ("Skott", 16)]

check_grown = lambda age: age[1] >= 18 
check_kids = lambda age: age[1] < 18

grown_friends = filter(check_grown, friends)
kid_friends = filter(check_kids, friends)

for i in kid_friends:
    print(*i)