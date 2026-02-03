
#Neeraj Khemani 24k-0548
class Vehicle:
  def __init__(self, vehicle_id, brand, rent_per_day ):
   self.vehicle_id = vehicle_id
   self.brand = brand 
   self.rent_per_day = rent_per_day 

  def display_details(self):
   print(f"Vehicle ID: {self.vehicle_id}")
   print(f"Brand: {self.brand}")
   print(f"Rent per day: {self.rent_per_day}")

  def calculate_rent(self,days):
    rent = days * self.rent_per_day 
    print("Total Rent: ", rent)


v1 = Vehicle(100, "Honda" , 7500)
v2 = Vehicle(101, "Suzuki" , 4500)

print("Vehicle 1 details:")
v1.display_details()
v1.calculate_rent(4)

print("\n")

print("Vehicle 2 details:")
v2.display_details()
v2.calculate_rent(6)
