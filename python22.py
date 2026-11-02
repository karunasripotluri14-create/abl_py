#2
name = input("Enter patient name: ")
age = int(input("Enter age: "))
if age <= 12:
    category = "Child"
elif age >= 60:
    category = "Senior"
else:
    category = "Adult"
print("1. Inpatient")
print("2. Outpatient")
choice = int(input("Enter choice: "))
if choice == 1:
     days = int(input("Enter admission days: "))
     bill = 1500 + days * 2500
else:
    bill = 300
consult = float(input("Consultation fee: "))
lab = float(input("Lab charges: "))
medicine = float(input("Medicine charges: "))
total = bill + consult + lab + medicine
total = total * 1.05
print("\n--- Hospital Bill ---")
print("Patient:", name)
print("Category:", category)
print("Total Bill: Rs.", round(total, 2))