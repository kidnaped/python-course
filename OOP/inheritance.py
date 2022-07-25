# inheritance = classes can inherit methods, atributes. 
# These calsses will have parent/child relations, where child recieves everything, that a parent class has
# And these classes can have children and give whatever they own to their children

class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):   # child calss from Animal
    def run(self):
        print("This rabbit is running")

class Fish(Animal):   # child calss from Animal
    def swim(self):
        print("This fish is swimming")

class Chyort(Animal):   # child calss from Animal
    def drink(self):
        print("This chyort is drinking")

rabbit = Rabbit()       # objects from created classes 
fish = Fish()
chyort = Chyort()

#print(rabbit.alive)
#fish.eat()
#chyort.sleep()

rabbit.run()
fish.swim()
chyort.drink()