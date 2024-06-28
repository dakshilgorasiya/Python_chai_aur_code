username = "chaiaurcode"

def func():
    username = "chai"
    print(username)

# func()
# print(username)


x = 99

def func2(y):
    z = x + y
    return z

# print(func2(1))


# def func3():
#     global x     #to get reference of x so it will modify global x
#     x = 88 

# func3()
# print(x)


# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# myResult = f1()

# myResult()

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

# print(f)
# print(g)

print(f(5))
print(g(5))