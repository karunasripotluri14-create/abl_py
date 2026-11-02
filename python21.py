#6
fares = {"Sleeper": 200, "AC": 500, "First Class": 1000}
name = input("Enter passenger name: ")
n = int(input("Enter number of passengers: "))
travel_class = input("Enter class (Sleeper/AC/First Class): ")
if n > 0 and travel_class in fares:
    total = fares[travel_class] * n
    print("Passenger:", name)
    print("Total Fare: Rs.", total)
else:
    print("Invalid input")
