#7
recorded = int(input("Enter recorded stock: "))
actual = int(input("Enter actual stock: "))
difference = actual - recorded
if difference == 0:
    print("Stock matches")
elif difference > 0:
    print("Extra stock:", difference)
else:
    print("Missing stock:", abs(difference))
