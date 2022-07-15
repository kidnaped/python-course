import random

x = random.randint(1,99)    # choses a random int from 1-99
y = random.random()         # choses a random float number between 0 and 1

rps = ["Rock", "Paper", "Scissors"]
z = random.choice(rps)      # choses one arg from list

deck = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(deck)        # shuffles the arg in the list

print(deck)