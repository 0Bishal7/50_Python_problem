# 40.Write a Python program to find the most frequent character in a string.
def most_frequent(s):
    frequency={}

    for char in s:
        if char in frequency:
            frequency[char] +=1
        else:
            frequency[char]=1

    max_count = -1
    most_frequent =""

    for char ,count in frequency.items():
        if count > max_count:
            max_count=count
            most_frequent =char

    return most_frequent

print(most_frequent("aaaabbbbbbbccc"))
