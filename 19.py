# 19.Write a Python program to find the sum of squares of all numbers in a given range.
def sum_of_squares(start, end):
    total = 0  # Initialize total to 0
    for i in range(start, end + 1):
        total += i ** 2  # Add the square of each number to total
    return total

print(sum_of_squares(1, 3))  # Output: 14

# Alternative
def sum_of_squares(start, end):
    return sum(i**2 for i in range(start, end + 1))
print(sum_of_squares(1, 6))  # Output: 14

