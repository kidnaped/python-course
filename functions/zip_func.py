# zip(*iterables) = aggregate elements from 2 or more iterables (list, tuple, set, etc.)
#                   creates a zip obj with paired elements stored in tuples for each element

login = ["Mr. One", "Happy Joe", "Jumper Jim"]
passwords = ("p@ssword", "!@#QWEASDZXC", "!QAZXSW@")
login_dates = ["1/1/2022", "6/4/2022", "13/5/2020"]

'''users = dict(zip(login, passwords))  # make zip obj and typecast it into dict

for key, value in users.items():
    print(key, ":", value)'''

users = zip(login, passwords, login_dates)

for i in users:
    print(i)