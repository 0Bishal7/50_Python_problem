# 33.Write a program to find the length of the longest substring without repeating characters.

def longest_unique_substring(s):
    seen = {}
    max_len = 0
    start = 0
    for i, char in enumerate(s):
        if char in seen and start <= seen[char]:
            start = seen[char] + 1
        else:
            max_len = max(max_len, i - start + 1)
        seen[char] = i
    return max_len
print(longest_unique_substring("abcabcbb"))  


