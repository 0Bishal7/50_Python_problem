# 49.Write a Python program to count the occurrences of each element in a list using a dictionary.

def count_ocurrences(lst):
    count ={}
    for item in lst:
        if item in count:
            count[item] +=1
        else:
            count[item] =1
    return count
print(count_ocurrences([1,2,3,1,1,2,3,33]))
        