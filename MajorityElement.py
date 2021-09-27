"""
Majority Element
================

@author: mhtehrani
July 20, 2021
https://github.com/mhtehrani

"""

def get_majority_element_fast(a):
    if len(a) == 1:
        return 1
    
    a.sort()
    mid = int(len(a)/2)
    if a.count(a[mid]) > mid:
        return 1
    else:
        return 0
    

n = int(input())
a = list(map(int, input().split()))

fast = get_majority_element_fast(a)
