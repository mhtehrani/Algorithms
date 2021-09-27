"""
Binary Search
=============

@author: mhtehrani
July 18, 2021
https://github.com/mhtehrani

"""

def binary_search_fast(a, key):
    if 0 > len(a)-1:
        return -1
    
    mid = int((len(a)-1)/2)
    if key == a[mid]:
        return mid
    elif key > a[mid]:
        temp = binary_search_fast(a[mid+1:len(a)], key)
        if temp == -1:
            return -1
        else:
            return mid+1 + temp
    else:
        return binary_search_fast(a[0:mid], key)


data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

ppp = []

for key in data2[1:]:
    ppp.append(binary_search_fast(data1[1:], key))

print(' '.join(map(str, ppp)))