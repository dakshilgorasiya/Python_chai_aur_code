tea_varities = ["Black", "Green", "Oolong", "White"]
# print(tea_varities)

# Accessing elements in a list
# print(tea_varities[0])

# slicing a list
# print(tea_varities[0:2])

# tea_varities[1:2] = "Herbal"  # This will not work as expected
# print(tea_varities)

# tea_varities[1:2] = ["Herbal"]
# print(tea_varities)

# tea_varities[1:3] = ["Herbal", "Fruit"]
# print(tea_varities)

# print(tea_varities[1:1]) # This will return an empty list

# tea_varities[1:1] = ["test", "test1"]
# print(tea_varities)

# tea_varities[1:2] = []
# print(tea_varities)

# for tea in tea_varities:
#     print(tea, end="-")

# if "Oolong" in tea_varities:
#     print("I have oolong tea")

# tea_varities.pop();
# print(tea_varities)

# tea_varities.append("Masala");
# print(tea_varities);

# tea_varities.remove("Green")
# print(tea_varities)

# tea_varities.insert(1, "Green")
# print(tea_varities)

# tea_varities_copy = tea_varities.copy() #it will create another reference in memory

squared_nums = [x**2 for x in range(10)] #list comprehension

print(squared_nums)

cube_nums = [y**3 for y in range(5)]
print(cube_nums)