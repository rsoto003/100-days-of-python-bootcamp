import random

coin_value = random.randint(0, 1)

print(coin_value)
if coin_value == 0:
    print("Heads")
else:
    print("Tails")

