# Write a program to calculate the sum of all the items in a list.

def sum_list(lst):
    return sum(lst)

print(sum_list([2,5,7]))

# Alternative

def sum_of_list(l):
    total=0
    for num in l:
        total += num
    return total
print(sum_of_list([5,8]))