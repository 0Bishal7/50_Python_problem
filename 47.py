# 47.Write a Python program to combine two dictionaries by adding values for common keys.
def combine_dict(dict1,dict2):
    combine_dict = dict1.copy()

    for key,Value in dict2.items():
        if key in combine_dict:
            combine_dict[key] +=Value
        else:
            combine_dict[key] =Value
    return combine_dict

print(combine_dict({'a':2,'b':2},{'a':3,'b':9}))