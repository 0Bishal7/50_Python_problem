# 25. Write a function that accepts any number of arguments and returns their sum.
def sum_args(*args):
    return sum(args)

print(sum_args(1,2,3,4,5,6))