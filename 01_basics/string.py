# '<string>' "<string>" """  <string>  """ are used to define strings

# chai = "Masala Chai"

# first_char = chai[0]
# print(first_char) 

# slice_chai = chai[0: 6]
# print(slice_chai)


# num_list = [0,1,2,3,4,5,6,7,8,9]
# print(num_list[0: 5: 2]) # slicing list

# print(chai.lower())

# print(chai.upper())

# print(chai.strip()) # removes leading and trailing whitespaces

# chai = "Lemon Chai"
# print(chai.replace("Lemon", "Masala")) # replaces Lemon with Masala
# print(chai) # string is immutable

# chai = "Lemon, Ginger, Masala, Mint"

# print(chai.split(", ")) # splits the string based on the delimiter and returns a list

# chai = "Masala Chai"

# print(chai.find("Chai")) # returns the index of the first occurence of the substring
# print(chai.find("chai")) # returns -1 if substring is not found

# chai = "Masala Chai Chai Chai"
# print(chai.count("Chai"))

# chai_type = "Masala"
# quantity = 2
# order = "I ordered {} cups of {} chai" # string formatting {} are placeholders

# print(order.format(quantity, chai_type)) # format method is used to replace the placeholders with the values

# chai_variety = ["Masala", "Ginger", "Lemon", "Mint"]

# print(", ".join(chai_variety)) # joins the list elements with the specified delimiter

# chai = "Masala Chai"
# print(len(chai)) # returns the length of the string

# for letter in chai:
#     print(letter)

# chai = "He said, \"Masala chai is awesome\" " # escape character

# chai = "Masala\nChai" # newline character
# print(chai)

# chai = r"Masala\nChai" # raw string
# print(chai)

chai = "Masala Chai"

print("Masala" in chai) # checks if the substring is present in the string