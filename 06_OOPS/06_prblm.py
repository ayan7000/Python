

class Car:
    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_car +=1

    def get_brand(self):
        return self.__brand +"! "
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    

    def fuel_type(self):
     
     return "petrol or diesel"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
       super().__init__(brand,model)
       self.battery_size=battery_size
    
    def fuel_type(self):
       return "electric charge"
    


    
# my_Tesla = ElectricCar("tesla","model s","85kWh")

# print(my_Tesla.fuel_type())
Car("tata" ,"safari")
Car("tata", "nexon")

print(Car.total_car)