def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i   # return terminate the function but yield pause the execution of function and save state and when again call it resume from before if calling it from different places python internally takes care of it and work for both differently

# for num in even_generator(10):
#     print(num)

a=  even_generator(5)