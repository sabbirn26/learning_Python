# Exercise 2 - Shopping cart Program

item = input("What are the item you want to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("How many would you like?:"))

total = price * quantity

print(f"You have bought{quantity} x {item}")
print(f"Your total price is: ${total}")