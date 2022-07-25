# map() = applies a func to each item in an iterable (list, tuple, etc.)
# map(func, iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda price: (price[0],price[1]*0.9)
to_dollars = lambda price: (price[0],price[1]/0.9)

store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    print(i)