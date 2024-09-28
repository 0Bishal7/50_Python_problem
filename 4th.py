# Create a program that takes a string as input and prints its reverse.
def reverse_string(s):
    return s[::-1]

print(reverse_string("Hello"))

# Explanation: [::-1] is slicing syntax to reverse the string.

#Alternative
def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str  
    return reversed_str

print(reverse_string("Hello")) 