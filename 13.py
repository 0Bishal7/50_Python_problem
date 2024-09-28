# 13.Write a program that counts the vowels in a given string?.
def vowel_counter(n):
    Vowels='aeiouAEIOU'
    count=0
    for i in n:
        if i in Vowels:
            count+=1
    return count
print(vowel_counter("Hello"))