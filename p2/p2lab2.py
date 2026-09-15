# nelson k
# 9/15/2026
# p2lab2

cars = {
    "camaro": 18.21,
    "prius": 52.36,
    "models s": 110,
    "silverado": 26,
}

print(cars)
car_keys = cars.keys()
print(car_keys)

car = input("enter a vehicle to see its mpg: ")
mpg = cars [car]
print (f"the mpg of a {car} is {mpg} miles per gallon.")

miles = float(input("how many miles will you drive the {car}"))
gallons_used = miles / mpg
print(f"driving a {car} for {miles} miles will use {gallons_used:.2f} gallons of gas.")