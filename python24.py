#4
bill = float(input("Enter bill amount: "))
if bill >= 5000:
   discount = bill * 0.10
elif bill >= 2000:
   discount = bill * 0.05
else:
   discount = 0
final_bill = bill - discount
print("Discount:", discount)
print("Final Bill:", final_bill)