# 20.Write a program to check if two strings are anagrams.


def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False  

    char_count = {}
    
    
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    
    
    for char in s2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False  
        else:
            return False 

    return True  

print(are_anagrams("listen", "silent"))  

# Alternative
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
print(are_anagrams("listen", "silent"))  

