import random

friends = ['Ariana', 'Rocky', 'Francine', 'Ryan', 'Max', 'Conky']

who_is_paying = random.randint(0, len(friends) - 1)

print(f"Oh, looks like {friends[who_is_paying]} is paying today!")
