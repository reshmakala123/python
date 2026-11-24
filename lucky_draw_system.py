
import random
import math

names = input("Enter customer names separated by commas: ")

names = names.split(",")

customers = list(set(name.strip() for name in names))

random.shuffle(customers)

total = len(customers)
print("\nTotal unique participants:", total)

if total >= 2:
    winners = random.sample(customers, 2)

    print("\nLucky Draw Winners!")

    for winner in winners:
        print(winner[::-1])

else:
    print("At least 2 participants are required.")

result = round(math.sqrt(total))

print("\nSquare root of participants:", result)
