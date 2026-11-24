
import random
import math

names = input("Enter guest names separated by commas: ")

name_list = names.split(",")

unique_names = []

for name in name_list:
    name = name.strip()

    if name not in unique_names:
        unique_names.append(name)

selected_name = random.choice(unique_names)

print("Selected Name:", selected_name)

reverse_name = selected_name[::-1]

print("Reversed Name:", reverse_name)

total_names = len(unique_names)

print("Total Unique Names:", total_names)

square_root = math.sqrt(total_names)

print("Rounded Square Root:", round(square_root))
