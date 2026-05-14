# Strings must be in quotes, and f-string needs quotes
staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    #print(f"Name is {name} and Age is {age}")
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break

else:
        print(f"No one is eligible to manage the staff")



