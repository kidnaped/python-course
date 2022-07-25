# object = instace of a class. It has attributes (what it has ex. name, age, height) and methods (what it does)

from class_car import Car

car_1 = Car("GAZ", "Niva", 1993, "Cherry")
car_2 = Car("VAZ", "Lada", 1995, "Wet Asphalt")

#car_1.drive()
#car_2.stop()

#car_1.wheels = 2
#car_2.wheels = 4

Car.wheels = 3

print(car_1.wheels)
print(car_2.wheels)