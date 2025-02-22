print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza would you like today? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0

# todo: work out how much they need to pay based on their size choice.
if size == "S":
    price += 5
elif size == "M":
    price += 10
else:
    price += 15
# todo: work out how much to add to their bill based on their pepperoni choice
if pepperoni == "Y":
    price += 2.50
# todo: work out their final amount based on whether or not they want cheese.
if extra_cheese == "Y":
    price += 1.50


print(f"Thank you for your patience, your price is: ${price:.2f}")
