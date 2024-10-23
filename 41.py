# 41.Write a Python program to remove the duplicates from a list.
def remove_duplicates(lst):
    unique_list=[]
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

print(remove_duplicates([1,2,2,3,3,44]))
