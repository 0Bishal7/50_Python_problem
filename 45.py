# 45.Write a program to flatten a nested list.
def flatten(lst):
    flat_list =[]
    for i in lst:
        for  item in i:
            flat_list.append(item)
    return flat_list

print(flatten([[2,3],[3,4,5],[8]]))