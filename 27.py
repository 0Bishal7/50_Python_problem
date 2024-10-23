# 27.Write a function to merge two lists without duplicates.
def merge_list(l1,l2):
    return list(set(l1+l2))

print(merge_list([3,5,7,8,9],[2,4,3,5,8,9]))