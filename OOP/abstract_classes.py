# abstract classes prevent user from creating an object of that class
# + compels(enforce) a user to override abstract methods in a child class

# abstract calss is more a template, an idea, a ghost class

# abstract class = a class containing ONE or more abstract methods
# abstract method = a method that has a declaration, but does not have an implementation
# in child class from abstract class we MUST override EVERY abstract method, or end up with error

from abc import ABC, abstractmethod     # abs abstract classes library

class Vehicle(ABC):                 # ABC as parent class makes our Vehicle class abstract
    
    @abstractmethod                 # @abstractmethod makes methods in our class abstract
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")
    
    def stop(self):
        print("You car has stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You motorcycle has stopped")

#vehicle = Vehicle()     # now we can't create object from Vehicle class, 
                        # cause its abstract nature, ending up with error
car = Car()
motorcycle = Motorcycle()

#vehicle.go()           # can't access to abstract methods directly either
car.go()
car.stop()
motorcycle.go()
motorcycle.stop()