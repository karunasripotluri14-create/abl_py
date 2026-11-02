#10

balance = 5000
pin = input("Enter PIN: ")
if pin == "1234":
    print("1. Check Balance")
    print("2. Withdraw Cash")
    choice = input("Enter choice: ")
    if choice == "1":
        print("Balance:", balance)
    elif choice == "2":
        amount = int(input("Enter amount: "))
        if 0 < amount <= balance:
            balance -= amount
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance or invalid amount")
    else:
        print("Invalid choice")
else:
    print("Invalid PIN")
