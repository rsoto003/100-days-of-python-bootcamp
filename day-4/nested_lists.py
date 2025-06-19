fruits = ['apple', 'banana']
vegetables = ['carrot', 'broccoli']

healthy_foods = [fruits, vegetables]

print(fruits)
print(vegetables)
print(healthy_foods)

junk_food = ['candy', 'fast food', 'ice cream']
print('***********************')
print(junk_food)

healthy_foods.append(junk_food)
print(healthy_foods)

print('***********************')
healthy_foods.remove(junk_food)
print(healthy_foods)
