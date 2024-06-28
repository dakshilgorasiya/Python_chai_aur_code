def sum_all(*args):         # "*" is mandatory
    print(*args)
    print(args)
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,4))
print(sum_all(1,2,3,4,5,6,7))