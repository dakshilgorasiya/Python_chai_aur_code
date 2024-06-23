# list is mutable(change in memory is possible)
# tuple is immutable

tea_types = ("Black", "Green", "Oolong")

# print(tea_types)

# tea_types[0] = "Lemon" #ERROR

more_tea = ("Herbal", "Earl Grey")

all_tea = more_tea + tea_types

# print(all_tea)

# if "Green" in all_tea:
    # print("I have green tea")

more_tea = ("Herbal", "Earl Grey", "Herbal")

# print(more_tea.count("Herbal"))

# (black, green, oolong) = tea_types  # lenght must be same it will create three variable and assign value of respective variable




