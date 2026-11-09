web_development = ["Anu", "Ammu", "Riya"]
data_science = ["Arun", "Asha", "Meera"]
ui_ux_design = ["Diya", "Kiran", "Niya"]


all_participants = [web_development, data_science, ui_ux_design]


web_development.append("Rahul")

data_science.insert(1, "Vishnu")

ui_ux_design.pop()

copied_data_science = data_science.copy()
data_science.clear()

print("First two Web Development participants:", web_development[:2])

name_lengths = [len(name) for name in copied_data_science]
print("Length of each name:", name_lengths)

print("Is Asha present:", "Asha" in web_development or "Asha" in copied_data_science or "Asha" in ui_ux_design)

first_participants = (web_development[0], copied_data_science[0], ui_ux_design[0])
print("First participants tuple:", first_participants)