# 35.Write a Python program to reverse words in a given sentence.
def reverse_words(s):
    return ' '.join(s.split()[::-1])

print(reverse_words("sayan roy"))