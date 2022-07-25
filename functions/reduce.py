# reduce() = apply a func to an iterable and reduce it ot a single cumulative value.
#            performs func on firs two elements and repeats process untill 1 value remains
#            we recycle elements within an iterable until 1 valur remains
# reduce(func, iterable)

import functools

#letters = ["H", "E", "L", "L", "O"]
#word = functools.reduce(lambda x, y: x + y, letters) # combine first two elements 
#                                                     # and assign it as new first element etc. until done
#print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)