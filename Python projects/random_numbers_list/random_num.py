import random

random_num = []

for i in range(0, 100, 10):
    group = list(range(i+1, i+11))
    test = random.choice(group)
    random_num.append(test)
print(random_num)