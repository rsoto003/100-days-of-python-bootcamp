import random
import my_module

random_number_0_to_1 = random.random() * 10

random_num = random.randint(1, 10)

random_float = random.uniform(1, 10)

my_module.my_function()
print(f"My name is {my_module.first_name} {my_module.last_name}. Random number is {random_number_0_to_1}")

print(random_num)

print(random_float)



