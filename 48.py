# 48.Write a Python program to iterate over dictionaries using for loops.
def iterate_dict(d):
    for key,value in d.items():
        print(f"{key}:{value}")

print(iterate_dict({'a':1,'b':2}))