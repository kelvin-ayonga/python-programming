import random
# states = ["Delaware", "Pensylvania","New Jersey"]


# states[2] = "Kenya"

# states.append("Kelvin Land")

# states.extend(["new land", "old land"])

# print(states)

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1 Option 
random_pick = random.randint(0, (len(friends) - 1))
print(friends[random_pick])

# 1 Option
print(random.choice(friends))