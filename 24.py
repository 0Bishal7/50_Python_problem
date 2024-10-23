# 24.Write a function that returns the greatest common divisor (GCD) of two numbers.

def GCD(a,b):
    while b:
        a,b =b,a%b
    return a

print(GCD(18,48))