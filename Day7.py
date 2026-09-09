#vehicle management system

class Vehicle:
    def start(self):
        print("Vehicle starts")


# Inheritance + Polymorphism
class Car(Vehicle):
    def start(self):
        print("Car starts")


class Bike(Vehicle):
    def start(self):
        print("Bike starts")


class Truck(Vehicle):
    def start(self):
        print("Truck starts")


# Objects
car = Car()
bike = Bike()
truck = Truck()


# Polymorphism
car.start()
bike.start()
truck.start()
