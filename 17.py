# 17.Write a program to find the sum of the digits of a given number.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
print(sum_of_digits(123)) 


