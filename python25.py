#5
plans = [("Basic", 10, 199),
         ("Standard", 25, 299),
         ("Premium", 50, 399)]
data = int(input("Enter required data (GB): "))
suitable = [p for p in plans if p[1] >= data]
if suitable:
    best = min(suitable, key=lambda p: p[2])
    print("Best Plan:", best[0])
    print("Monthly Cost: Rs.", best[2])
else:
    print("No suitable plan found")