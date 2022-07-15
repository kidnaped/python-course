# dictionary = a changable, unordered collection of unique key:value pairs
#              Fast, because use hashing, allow us to access value quickly

capitals = {"USA":"Washington",
            "India":"New Dehly",
            "China":"Beijing",
            "Russia":"Moscow"}

capitals.update({"Germany":"Berlin"})   #adds new key:value pair in our dictionary
capitals.update({"USA":"Los Santos"})   #updates existing pair with new value
capitals.pop("USA")                     #removes selected pair by its key
capitals.clear()

#print(capitals["Russia"])
#print(capitals.get("Germany"))      #checks if there is certain key:value pair in dictionary
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())              #prints every key:value pair in dictionary

for key, value in capitals.items():
    print("Country: " + key, "Capital: " + value)
