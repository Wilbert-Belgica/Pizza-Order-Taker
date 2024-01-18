print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size of pizza do you want? (S, M, or L) \n ")
add_pepperoni = input("Do you want extra pepperoni? (Y or N) \n ")
extra_cheese = input("Do you want extra cheese? (Y or N \n) ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
price = 0
if size == "S":
 price += 15
elif size == "M":
 price += 20
elif size == "L":
 price += 25

if add_pepperoni == "Y":
 price += 2

if extra_cheese == "Y":
 price += 1

 print(f"Your final bill is: ${price}.")