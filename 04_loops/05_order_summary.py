names = ["Hitesh", "Meera", "Sam", "Ali"]
#[](){}{key:value}

bills = [50,70,100,55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")