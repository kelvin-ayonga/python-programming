import random
import my_module

# random_intger = random.randint(1, 10)
# print(random_intger)

# print(my_module.my_favourite_number)


# random_number_0_to_1 = random.random() * 100000
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)


random_choice = random.randint(0,1)

if random_choice == 0: 
    print("Heads")
else:
    print("Tails")