#  Basic Syntax and Data Types

#1.Write a program to check if a number is even or odd.


def check_function_odd_or_even(number):
    if number % 2 == 0:
        return "Even number"
    else:
        return "odd number"
    

print(check_function_odd_or_even(2))    



# Explanation: If a number is divisible by 2 (number % 2 == 0), it's even; otherwise, it's odd.

