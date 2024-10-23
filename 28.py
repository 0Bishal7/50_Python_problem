# 28.Write a function that takes a list of numbers and returns a list of their squares.
def square_list(l):
    square_list =[]
    for i in l:
        square_list.append(i**2)
    return square_list
print(square_list([6,7,84,4]))


