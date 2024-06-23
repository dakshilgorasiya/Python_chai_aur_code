chai_types = {
    "Masala": "Spicy",
    "Ginger": "Zesty",
    "Green": "Mild"
}

# print(chai_types)

# print(chai_types["Masala"])

# print(chai_types["IJOIJ"])
# print(chai_types.get("oijoij"))  #If not find will not give error

chai_types["Green"] = "Fresh" #To change value

# print(chai_types)

# for chai in chai_types:    #chai is index
#     print(chai, chai_types[chai])

# for key, value in chai_types.items():    #key, value loop only work on dictionary items so we call items method
#     print(key, value)

# if "Masala" in chai_types:
#     print("I have masala chai")

# print(len(chai_types))

# chai_types["Earl Grey"] = "Citrus"
# print(chai_types)

# chai_types.pop("Ginger")
# print(chai_types)

# chai_types.popitem()  #Remove last added item
# print(chai_types)

# del chai_types["Green"]
# print(chai_types)

# chai_types_copy = chai_types.copy() #to create new reference

tea_shop = {
    "chai": {
        "Masala": "Spicy",
        "Ginger": "Zest"
    },
    "Tea": {
        "Green": "Mild",
        "Black": "Strong"
    }
}

# print(tea_shop)

# print(tea_shop["chai"])

# print(tea_shop["chai"]["Ginger"])

squared_num = {x:x**2 for x in range(6)}
# print(squared_num)

squared_num.clear() # to delete all dictinary
# print(squared_num)

keys = ["Masala", "Ginger", "Lemon"]

default_value = "Delicious"

# new_dict = dict.fromkeys(keys, default_value)
# print(new_dict)

