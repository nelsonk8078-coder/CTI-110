 # kyler nelson
 # 9/10/2026
 # p1hw2
 # travel expenses

print("----------Travel Budgeter----------")

print("\n")

print("This will help calculate/display travel expenses")

print("\n")

location = input("Enter your travel destination: ")
budget = int(input("Enter you budget: $ "))
gas = int(input("How much doy you think you will spend on gas? $ "))
accomodation = int(input("Appoximentely, how much wil you need for accomodation/hotel? $ "))
food = int(input("Last how much will you need for food? $ "))
remaning = budget - gas - accomodation - food

print("\n\n")

print("------Travel Expenses------")
print("Location:", location)
print("Intial Budget: $", budget)
print("Gas: $", gas)
print("Hotel Price: $", accomodation)
print("Food: $", food)
print("Reamaining Balance: $", remaning)