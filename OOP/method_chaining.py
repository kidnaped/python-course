# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

#car.turn_on()       # calling methods usual way
#car.drive()

#car.turn_on().drive()   # when executing precious method it returns self(car) as object
                        # and imediately executes car.drive() method
                        # car.turn_on()->returns car->car.drive()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()         # here "\" is used as line continuation character