# the class is used as a blueprint, which we can use to create different instances and objects from it
class Car:

    wheels = 4  # class variable, declares out of constructor 
                # every object will always had a copy of this var
                # but in class definition we assign a default value 

    def __init__(self, make, model, year, color):     # constuctor, that constructs objects for us and accepts some parameters
        self.make = make        # instance variables, each object can assign different values to them
        self.model = model      # instance variables
        self.year = year        # instance variables
        self.color = color      # instance variables

    def drive(self):
        print(f"This {self.model} is diving")
    
    def stop(self):
        print(f"The {self.model} has stopped")
