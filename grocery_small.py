fruits = ["Apple", "Banana", "orange"]
vegetables = ["Carrot", "Potato", "onion"]
beverages = ["Water", "Coffee", "Tea"]

fruits.append("cherry")

vegetables.insert(1, "cucumber")

beverages.pop()

inventory = [fruits, vegetables, beverages]
print("Inventory management state complete.")
print(f"Current Inventory: {inventory}")

print("First two fruits:", fruits[:2])

print("Last item in vegetables list:", vegetables[-1])

fruits_lengths =[len(fruits)for fruits in fruits]
print("lenghts of items in fruits list:",fruits_lengths)

is_water_in_beverages = "Water" in beverages
print("Is'Water'in the beverages list?",is_water_in_beverages)

first_item_tuples=(fruits[0],vegetables[0],beverages[0])
print("Tuple of the first item from the each section:",first_item_tuples)
