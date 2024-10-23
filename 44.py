# 44.Write a program to merge two sorted lists into one sorted list.
def two_sorted_list(lst1,lst2):
    return sorted(lst1+lst2)

print(two_sorted_list([2,3,4,5,5,5],[2,7,8,9,4]))


