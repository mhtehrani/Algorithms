"""
Largest Number
==============

@author: mhtehrani
July 14, 2021
https://github.com/mhtehrani

"""

def is_greater(a,b):
    if int(a+b) >= int(b+a):
        return True
    else:
        return False

def largest_number_fast(temp):
    Max_number = ''
    a = temp[:].split()
    if len(a) == 1:
        return a
    
    while len(a) > 1:
        largest_value = a[0]
        for i in range(len(a)):
            if is_greater(a[i],largest_value):
                largest_value = a[i]
                index = i
            
        
        Max_number = Max_number+largest_value
        del a[index]
    
    
    return Max_number+a[0]

temp = input()
print(largest_number_fast(temp))