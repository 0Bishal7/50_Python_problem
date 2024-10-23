# 31.Write a Python program to count the occurrences of each word in a string.
def count_string(s):
    words=s.split()
    words_count ={}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return words_count

print(count_string("oh hi sayan is here . hi sayan"))
