# Write a program to find the largest number in a list.

def find_largenumber(l):
    return max(l)

print(find_largenumber([1,69,7,9]))

#Alternative

def lagernumber(l):
    largest=l[0]
    for num in l:
        if num >  largest:
            largest= num
    return largest

print(lagernumber([2,3,69,65]))