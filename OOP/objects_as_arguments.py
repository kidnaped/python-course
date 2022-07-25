class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle, color):
    
    vehicle.new_color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()
bike_2 = Motorcycle()
bike_3 = Motorcycle()

change_color(car_1, "blue")
change_color(car_2, "green")
change_color(car_3, "bloody")
change_color(bike_1, "black")
change_color(bike_2, "iron")
change_color(bike_3, "purple")

print(car_1.new_color)
print(car_2.new_color)
print(car_3.new_color)
print(bike_1.new_color)
print(bike_2.new_color)
print(bike_3.new_color)