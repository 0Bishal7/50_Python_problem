
# 11. Write a program to print the Fibonacci sequence up to n terms.

def fibonacci(n):
    a, b = 0, 1  
    count = 0    
    while count < n:
        print(a, end=' ')
        temp = a  
        a = b     
        b = temp + b  
        count += 1 
print(fibonacci(5))


















