print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza would you like today? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")
price = 0

# todo: work out how much they need to pay based on their size choice.
# todo: work out how much to add to their bill based on their pepperoni choice
# todo: work out their final amount based on whether or not they want cheese.


if size == 'S':
    price += 15
    if pepperoni == 'Y':
        price += 2
elif size == 'M':
    price += 20
    if pepperoni == 'Y':
        price += 3
elif size == 'L':
    price += 25
    if pepperoni == 'Y':
        price += 3
else:
    pepperoni = input("Please enter a valid size. You can choose S or M or L: ") # need to figure out how to reloop this process and start over if user selects invalid pizza size.

if cheese == 'Y':
    price += 1

print(f"Thank you for your patience, your price is: ${price:.2f}")
