# nested loops =    The "inner loop" will finish all of its iterations before
#                   finishing one iteration of the "outer loop"

# creating a rectangle of symbols of our choise
rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")   # second argument (end="") prevents cutsor moving to the next line
    print()
