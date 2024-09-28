# Write a Python program to find the second largest number in a list.
def second_largest(l):
    unique_list = list(set(l))
    unique_list.sort()
    return unique_list[-2]

print(second_largest([3,4,9,12,34,15]))

# Alternative
def sec_large(l):
    first=second =float('-inf')
    for i in l:
        if i > first:
            second=first
            first = i
        elif i > second and i !=first:
            second=i
    return second

print(sec_large([3,4,9,12,34,15]))
