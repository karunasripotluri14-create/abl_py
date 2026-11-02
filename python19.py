#9
vehicle = input("Enter vehicle (car/bike): ").lower()
hours = int(input("Enter parking hours: "))
if vehicle == "car":
    fee = 30 * hours
elif vehicle == "bike":
    fee = 15 * hours
else:
    fee = -1
if fee >= 0 and hours > 0:
    print("Parking fee: Rs.", fee)
else:
    print("Invalid input")
