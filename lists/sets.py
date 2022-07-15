# set = collection which unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)                 #adds values from another set to it
#dinner_table = utensils.union(dishes)    #unites two sets under new one

#print(utensils.difference(dishes))      #checks the difference of items in sets and returns different item from main set
                                        #What utensils has that dishes doesn't? {fork, spoon}
print(utensils.intersection(dishes))    #checks the intersections between two sets and returns its value

#for i in dinner_table:
#    print(i)