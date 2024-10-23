# 39.Write a Python program to check if two strings are rotation of each other.
def are_rotation(s1,s2):
    if len(s1) != len(s2):
        return False
    
    for i in range(len(s1)):
        if s1[i:] +s1[:i] == s2:
            return True
    return False

print(are_rotation("abc","cba"))
     
