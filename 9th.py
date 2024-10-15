# 9.Write a program to remove duplicates from a list.

def r_duplicates(l):
 return list(set(l))


print(r_duplicates([2,2,3,6,9,7,6]))


# Alternative
def remove_duplicates(l):
    list=[]
    for i in l:
       if i not in list:
          list.append(i)
    return list

print(remove_duplicates([4,5,7,98,8,98]))

