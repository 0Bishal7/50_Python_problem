# Python Basics: 50 Coding Questions & Answers 💻🐍

Welcome to **Python Basics**, where you'll find solutions to 50 common coding challenges in Python! This repository is a collection of beginner to intermediate Python problems with detailed explanations and solutions. Whether you're preparing for an interview, brushing up on your Python skills, or learning the language for the first time, this guide will help you level up!

---

## Table of Contents 📋

1. [Basic Python Syntax](#basic-python-syntax)
2. [Control Flow](#control-flow)
3. [Functions](#functions)
4. [Strings](#strings)
5. [Lists, Tuples, and Dictionaries](#lists-tuples-and-dictionaries)

---

## Basic Python Syntax 📝

1. **Print "Hello, World!"**
    ```python
    print("Hello, World!")
    ```

2. **Sum of Two Numbers**
    ```python
    def sum_two(a, b):
        return a + b
    print(sum_two(3, 5))  # Output: 8
    ```

3. **Check if a Number is Even or Odd**
    ```python
    def is_even(num):
        return num % 2 == 0
    print(is_even(4))  # Output: True
    ```

---

## Control Flow 🚦

4. **Find the Largest Number Among Three**
    ```python
    def largest_of_three(a, b, c):
        return max(a, b, c)
    print(largest_of_three(10, 20, 15))  # Output: 20
    ```

5. **FizzBuzz Problem**
    ```python
    def fizzbuzz(n):
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
    fizzbuzz(15)
    ```

6. **Factorial of a Number (Using Recursion)**
    ```python
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)
    print(factorial(5))  # Output: 120
    ```

---

## Functions 🛠️

7. **Check if a Number is Prime**
    ```python
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    print(is_prime(11))  # Output: True
    ```

8. **Find GCD of Two Numbers**
    ```python
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    print(gcd(48, 18))  # Output: 6
    ```

9. **Fibonacci Sequence**
    ```python
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[:n]
    print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    ```

---

## Strings 📚

10. **Count the Occurrences of Each Word in a String**
    ```python
    def count_words(s):
        words = s.split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return word_count
    print(count_words("hello world hello"))  # Output: {'hello': 2, 'world': 1}
    ```

11. **Check if a String is a Palindrome**
    ```python
    def is_palindrome(s):
        return s == s[::-1]
    print(is_palindrome("racecar"))  # Output: True
    ```

12. **Find the Length of the Longest Substring Without Repeating Characters**
    ```python
    def longest_unique_substring(s):
        seen = {}
        max_len = 0
        start = 0
        for i, char in enumerate(s):
            if char in seen and start <= seen[char]:
                start = seen[char] + 1
            else:
                max_len = max(max_len, i - start + 1)
            seen[char] = i
        return max_len
    print(longest_unique_substring("abcabcbb"))  # Output: 3
    ```

---

## Lists, Tuples, and Dictionaries 📦

13. **Remove Duplicates from a List**
    ```python
    def remove_duplicates(lst):
        return list(set(lst))
    print(remove_duplicates([1, 2, 2, 3]))  # Output: [1, 2, 3]
    ```

14. **Merge Two Sorted Lists**
    ```python
    def merge_sorted_lists(lst1, lst2):
        return sorted(lst1 + lst2)
    print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
    ```

15. **Sort List of Dictionaries by a Specified Key**
    ```python
    def sort_by_key(lst, key):
        return sorted(lst, key=lambda x: x[key])
    print(sort_by_key([{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}], 'age'))
    # Output: [{'name': 'Jane', 'age': 22}, {'name': 'John', 'age': 25}]
    ```

16. **Find the Intersection of Two Lists**
    ```python
    def intersection(lst1, lst2):
        return list(set(lst1) & set(lst2))
    print(intersection([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]
    ```

17. **Combine Two Dictionaries (Adding Values for Common Keys)**
    ```python
    from collections import Counter

    def combine_dicts(dict1, dict2):
        return dict(Counter(dict1) + Counter(dict2))
    print(combine_dicts({'a': 1, 'b': 2}, {'a': 2, 'b': 3}))  # Output: {'a': 3, 'b': 5}
    ```

---

## How to Use 🛠️

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/python-basics.git
    ```
2. **Navigate to the project folder**:
    ```bash
    cd python-basics
    ```
3. **Run the Python file** with any solution you want:
    ```bash
    python <filename>.py
    ```

---

## Contributions 🎯

Feel free to contribute by adding more coding challenges or improving the existing ones. Fork this repository, make your changes, and submit a pull request!

---

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Let's Connect! 💬

- [LinkedIn](https://www.linkedin.com/in/yourprofile)
- [Portfolio](https://yourportfolio.com)

---

**Happy Coding!** ✨
