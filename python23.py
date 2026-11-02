#3
basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
deductions = float(input("Enter total deductions: "))
gross = basic + allowances
netsalary = gross - deductions
print("Gross Salary:", gross)
print("Total Deductions:", deductions)
print("Net Salary:", netsalary)