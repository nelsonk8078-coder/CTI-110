# cti 110
# p2h1 - setup only
# talk about how to format the display

destination = "Raleigh"
budget = 2000
expenses = 1000
remaining = budget - expenses


print(f"{"Destination:":15} {destination:<20}")
print(f"{"Budget:":<15} ${budget:<15.2f}")
print(f"{"Expenses:":<15} ${expenses:<15.2f}")
print(f"{"Remaining:":<15} ${remaining:<15.2f}")
