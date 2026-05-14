flavours = ["ginger", "out of stock", "lemon", "Discontinued", "Tulsi"]


for flavour in flavours:
    if flavour == "out of stock":
        continue

    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break

    print(f"{flavour} item found")

print(f"out side of loop")

