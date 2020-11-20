class Car:
	def __init__(self,wheels_number,car_doors,passengers):
		self.wheels_number = wheels_number
		self.car_doors = car_doors
		self.passengers = passengers
class SUV:
	def __init__(self,brand_name,air_bag,sunroof):
		self.brand_name = brand_name
		self.air_bag = air_bag
		self.sunroof = sunroof
car_a = Car(4,4,4)
car_b = Car(4,4,4)
suv_a = SUV(0,4,True)
suv_b = SUV(0,4,True)
suv_a.brand_name = input()
car_a.car_doors = int(input())
suv_a.air_bag = int(input())
suv_b.brand_name = input()
car_b.car_doors = int(input())
suv_b.air_bag = int(input())
print("==== Details ====")
print("Brand:",suv_a.brand_name)
print("Wheels number:",car_a.wheels_number)
print("Doors number:",car_a.car_doors)
print("Air-bags number:",suv_a.air_bag)
print("Sunroof:",suv_a.sunroof)
print("=================")
print("==== Details ====")
print("Brand:",suv_b.brand_name)
print("Wheels number:",car_b.wheels_number)
print("Doors number:",car_b.car_doors)
print("Air-bags number:",suv_b.air_bag)
print("Sunroof:",suv_b.sunroof)
print("=================")
print(suv_a.air_bag<suv_b.air_bag)
print(car_a.car_doors>car_b.car_doors)