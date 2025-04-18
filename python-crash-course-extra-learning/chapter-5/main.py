# checking if lists are empty
pizza_toppings = []


def check_toppings(toppings):
    if toppings:
        print("We have toppings to add on the pizza")
    else:
        print("need to add toppings")


check_toppings(pizza_toppings)

pizza_toppings.append("pepperoni")

check_toppings(pizza_toppings)

