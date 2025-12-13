from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id, brand, rental_price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.rental_price = rental_price

    @abstractmethod
    def total_rental_cost(self):
        pass

    @abstractmethod
    def display_vehicle_details(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_id, brand, rental_price, number_of_doors):
        super().__init__(vehicle_id, brand, rental_price)
        self.number_of_doors = number_of_doors

    def total_rental_cost(self, days):
        total_money = days * self.rental_price
        print("Total Cost For Car is ", total_money)

    def display_vehicle_details(self):
        print("Vehicle type ", self.brand)
        print("Vehicle id ", self.vehicle_id)
        print("Rental Price per Day is ", self.rental_price)
        print("Number of Doors in car is ", self.number_of_doors)


class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, rental_price, bike_type):
        super().__init__(vehicle_id, brand, rental_price)
        self.bike_type = bike_type

    def total_rental_cost(self, days):
        total_money = days * self.rental_price
        print("Total Cost For Bike  is ", total_money)

    def display_vehicle_details(self):
        print("Vehicle type ", self.brand)
        print("Vehicle id ", self.vehicle_id)
        print("Rental Price per Day is ", self.rental_price)
        print("bike type is ", self.bike_type)


ToyotaCar = Car("123","ToyotaCar",2500,6)
ToyotaCar.total_rental_cost(2)
ToyotaCar.display_vehicle_details()


Dominar_400 = Bike("1234","DominarBajaj",2000,"400CC Engine")
Dominar_400.display_vehicle_details()
Dominar_400.total_rental_cost(2)