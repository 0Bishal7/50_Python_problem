# 32.Write a Python program to find all substrings of a string.
def all_substrings(s):
    substrings =[]
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            substrings.append(s[i:j])
    return substrings
print(all_substrings("abc"))

     