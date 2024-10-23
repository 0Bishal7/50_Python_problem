# 16.How can you check if a string is a palindrome?
def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True

print(is_palindrome("madam"))  


# Alternative
def palindrome(s):
    return s == s[::-1]
print(palindrome("madam"))


