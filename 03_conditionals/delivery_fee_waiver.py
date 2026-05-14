order_amount = int(input("Enter the order amount: "))

print(f"Order Amount: {type(order_amount)}")


deliver_fees = 0

if order_amount > 300:
    deliver_fees = 0
    print(deliver_fees)


else:
    print(f"Delivery fess is: {deliver_fees+30}")
          
#terniary operator
print("$$$$")
deliver_fee = 0 if order_amount > 300 else 30

print(f"Delivery fess is: {deliver_fee}")