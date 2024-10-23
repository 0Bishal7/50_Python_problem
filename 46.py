# 46.Write a Python program to find the intersection of two lists.
def intersection(l1,l2):
    return list(set(l1) & set(l2))

print(intersection([2,3,4,5],[5,6,7,3]))
