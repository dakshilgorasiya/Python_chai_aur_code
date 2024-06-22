n1 = 10
n2 = n1
n2 = 20
print(n1, n2)  # 10 20


l1 = [1, 2, 3]
l2 = l1
print(l1, l2)  # [1, 2, 3] [1, 2, 3]

l2[0] = 100
print(l1, l2)  # [100, 2, 3] [100, 2, 3]


l3 = [1, 2, 3]
l4 = l3
l4 = [1, 2, 3]
print(l3, l4)  # [1, 2, 3] [1, 2, 3]
l3[0] = 55
print(l3, l4)  # [55, 2, 3] [1, 2, 3]


a = [1, 2, 3]
b = a[:] # Copy whole list
print(a, b)  # [1, 2, 3] [1, 2, 3],

x = [1, 2, 3]
y = x
print(x == y, x is y)  # True True

y = [1, 2, 3]
print(x == y, x is y)  # True False