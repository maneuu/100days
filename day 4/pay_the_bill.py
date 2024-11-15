import random
names = ["Alice", "Bob", "Charlie", "Diana"]  
will_pay = random.randint(0, len(names) - 1)
print(f"{names[will_pay]} is going to buy the meal today!")
