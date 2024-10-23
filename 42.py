# 42.Write a Python program to convert a list of tuples into a dictionary.
def tuple_to_dict(tuples):
    result ={}
    for key ,value in tuples:
        result[key]=value
    return result
print(tuple_to_dict([('a',1),('b',2)]))