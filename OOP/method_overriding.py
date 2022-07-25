class Animal:
    def eat(self):                      # method name+(parameters) are called method signature
        print("This animal is eating")
        
class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot") # to override method from parent class
                                                # to be more specific create a method with the same signature
                                                # and define new behavior

rabbit = Rabbit()
rabbit.eat()