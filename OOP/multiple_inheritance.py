# multiple inheritance = when a child class is derived from more than one parent class

class Predator:

    def hunt(self):
        print("This animal is hunting")

class Prey:

    def flee(self):
        print("This animal fees")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator, Prey):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()