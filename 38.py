# 38. Write a program to capitalize the first and last letter of each word in a string.

def capitalize_1st_lst(s):
    words = s.split()
    result =[]
    for word in words:
        if len(word)>1:
            new_record = word[0].upper()+word[1:-1]+word[-1].upper()
        else:
            new_record = word.upper()
        result.append(new_record)
    return ''.join(result)

print(capitalize_1st_lst("Hello world"))
