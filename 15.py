# 15.Write a Python program to print numbers from 1 to 100, but for multiples of 3 print "Fizz" instead of the number, and for multiples of 5 print "Buzz".
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizz_buzz()


