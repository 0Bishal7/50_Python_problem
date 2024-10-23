# 30.Write a function to find the minimum and maximum values in a list.
def min_max(lst):
    max_list = min_list = lst[0]
    for i in lst:
        if i < min_list:
            min_list =i
        if i > max_list:
            max_list = i
    return min_list,max_list
print(min_max([4,6,7]))


