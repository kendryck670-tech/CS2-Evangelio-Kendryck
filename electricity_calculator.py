# Electricity Bill Calculator
RATE = 12.90
while True:
    name = input("Enter customer name: ")
    if name.strip() != "":
        break
    else:
        print("Name cannot be blank!")
while True:
    previous = input("Enter previous meter reading: ")
    try:
        previousreading = float(previous)
        if previousreading != "":
            break
        else:
            print("Invalid Reading!")
    except ValueError:
        print("Must be a positive number")
while True:
    current = float(input("Enter current meter reading: "))
    try:
        currentreading = float(current)
        if currentreading != "":
            break
        else:
            print("Invalid Reading!")
    except ValueError:
        print("Must be a positive number")
consumption = currentreading-previousreading
total_bill = consumption * RATE

print("Customer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
