class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand     #if we use __ before variable name then it will beacome private
        self.__model = model
        Car.total_car += 1   #self.total_car += 1

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are amazing"
    
    @property
    def model(self):
        return self.__model
    

my_car = Car("Toyota", "Corolla")
# print(my_car.model)
# print(my_car.brand)    
# print(my_car.get_brand())
# print(my_car.general_description())
# print(Car.general_description())
# my_car.model = "j"
# print(my_car.model)



my_new_car = Car("Tata", "Safari")
# print(my_new_car.full_name())
# print(my_new_car.fuel_type())


#inheritance
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model) # to call parent's controcter
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
# print(my_tesla.full_name())
# print(my_tesla.battery_size)
# print(my_tesla.fuel_type())

# print(Car.total_car)

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))


class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())