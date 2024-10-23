# 37.Write a program to check if a string contains only digits.
def is_digit_string(s):
    for char in s:
        if not("0" <=char <= "9"):
            return False
    return True

print(is_digit_string("9099"))

