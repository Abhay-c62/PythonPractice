#Define the parent class to hold general data
class Vehicle:
    #The initializer method runs automatically when an object is created from the class
    def __init__(self, brand, year):
        self.brand = brand #store the brand of the vehicle
        self.year = year #store the year of manufacture of the vehicle
    #A method that format and returns the vehicle information
    def display_info(self):
        return f"{self.brand} {self.year}" 
    
class Car(Vehicle):
    #'pass' is placeholder showing the vehicle Info
    pass
#Create a new object (instance) of the car class
#then automatically calls the __init__ method inherited from vehicle
my_car=Car("Mercedes-Benz", 2026)
print(my_car.display_info())