#36. Write a Python program to remove all punctuation marks from a string.
def remove_punctuation(s):
    result = ''
    for char in s:
       if char.isalnum() or char.isspace():
        result += char
    return result


print(remove_punctuation("hello, world!"))  
