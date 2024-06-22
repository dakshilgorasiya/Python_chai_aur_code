
# from decimal import Decimal
# from fractions import Fraction
import math
import random

# x = 2
# y = 3
# z = 4

# print(x + y)

# print(x ** y)

# print(40 + 2.23)

# # print('dakshil' + 7) # TypeError: can only concatenate str (not "int") to str

# print(int(2.23))

# print(float(2))

# print (float(40) + 2.23)

# print('dakshil' + 'gorasiya')

# # print(2 ** 1000) # capability of python

# print(x < y < z)

# print(x < y and y < z)

# print(math.floor(2.3))

# print(math.floor(-2.3))

# print(math.trunc(2.3)) # give integer near to 0

# print(math.trunc(-2.3))

# print(2 + 1j) # complex number

# print((2 + 1j) * 2)

# print(0o10) # octal number

# print(0x10) # hexadecimal number

# print(0b10) # binary number

# print(oct(64)) # convert to octal
# #or
# print(int('64', 8)) # 64 is decimal 8 is base

# print(hex(64)) # convert to hexadecimal

# print(int('64', 16)) # 64 is decimal 16 is base

# print(bin(64))  # convert to binary

# print(int('1000', 2)) # 64 is decimal 2 is base

# print(random.random())

# print(random.randint(1, 10)) # 1 to 10 including 1 and 10

# print(random.choice(['a', 'b', 'c'])) # random choice from list

# l1 = [1, 2, 3, 4, 5]

# random.shuffle(l1) # shuffle list

# print(l1)

# print(0.1+0.1+0.1-0.3) # problem with floating point arithmetic

# Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') # use decimal module to solve this problem

# myFra = Fraction(6, 9)

setone = {1, 2, 3, 4}
# print(setone)

# print(setone | {3, 4, 5, 6}) # union

# print(setone & {3, 4, 5, 6}) # intersection

# print(setone - {3, 4, 5, 6}) # difference

print(setone - {1,2,3,4}) # to initialize empty set use set() not {} because {} is used for dictionary

print(type(setone - {1,2,3,4}))