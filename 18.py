# 18.Write a program to print the first n prime numbers.
def first_n_primes(n):
    primes = []  
    num = 2  
    
    while len(primes) < n:  
        is_prime = True 
        
        for i in range(2, int(num ** 0.5) + 1):  
            if num % i == 0:  
                is_prime = False
                break  
        
        if is_prime: 
            primes.append(num)  
        num += 1 
    print(primes)  

first_n_primes(5) 





