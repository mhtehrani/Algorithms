"""
3-way Quick Sort
================

@author: mhtehrani
July 22, 2021
https://github.com/mhtehrani

"""

import random

def partition3(a, l, r):
    x = a[l]
    left = l
    right = l
    for i in range(l + 1, r + 1):
        if a[i] == x:
            right += 1
            a[i], a[right] = a[right], a[i]
        elif a[i] < x:
            right += 1
            a[i], a[right] = a[right], a[i]
            a[left], a[right] = a[right], a[left]
            left += 1
    # a[l], a[j] = a[j], a[l]
    return left, right

def randomized_quick_sort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    
    m, n = partition3(a, l, r)
    
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, n + 1, r);


n = int(input())
a = list(map(int, input().split()))

randomized_quick_sort3(a, 0, n - 1)
print(' '.join(map(str, a)))
