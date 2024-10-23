# 34.Write a Python program to convert a string to title case without using built-in functions.
def to_title_case(s):
    result =[]
    words = s.split()
    for i in words:
        if i :
             result.append(i[0].upper()+i[1:].lower())
    return ' '.join(result)

print(to_title_case("sayan roy"))