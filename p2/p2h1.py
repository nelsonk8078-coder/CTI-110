# cti 110
# Nelson k
# p2h1 
# travel budgeter expanded

#test code from set up 
#location = "Raleigh"
#budget = 2000
#expenses = 1000
#remaining = budget - expenses

print("----------Travel Budgeter----------")

print("\n")

print("This will help calculate/display travel expenses")

print("\n")

location = input("Enter your travel destination: ")
budget = float(input("Enter you budget: $ "))
gas = float(input("How much doy you think you will spend on gas? $ "))
accomodation = float(input("Appoximentely, how much wil you need for accomodation/hotel? $ "))
food = float(input("Last how much will you need for food? $ "))
remaining = budget - gas - accomodation - food

print("\n\n")

#code from set up
#print(f"{"location:":15} {location:<20}")
#print(f"{"Budget:":<15} ${budget:<15.2f}")
#print(f"{"Expenses:":<15} ${expenses:<15.2f}")
#print(f"{"Remaining:":<15} ${remaining:<15.2f}")

print("----------Travel Expenses----------")
print(f"{"Location:":<15} {location:<15}")
print(f"{"Intial Budget:":<15} ${budget:<15.2f}")
print(f"{"Gas:":<15} ${gas:<15.2f}")
print(f"{"Accomodation:":<15} ${accomodation:<15.2f}")
print(f"{"Food:":<15} ${food:<15.2f}")
print(f"{"Remaining:":<15} ${remaining:<15.2f}")
print("-----------------------------------")