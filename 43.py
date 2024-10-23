# 43.Write a Python program to sort a list of dictionaries by a specified key.
def sort_by_key(lst, key):
    def get_key_value(item):
        return item[key]
    return sorted(lst,key=get_key_value)

print(sort_by_key([{'name':'sayan','age':62},{"name":"bishal","age":34}],'age'))