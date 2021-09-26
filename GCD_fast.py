"""
Last Digit of a Large Fibonacci Number
======================================

@author: mhtehrani
July 1, 2021
https://github.com/mhtehrani

"""
# Uses python3
# import sys
import timeit

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_fast(a, b):
    while True:
        if a % b == 0:
            break
        else:
            c = a % b
            a = b
            b = c
    return b


a, b = map(int, input().split())

a1 = timeit.default_timer()
# print(gcd_naive(a, b))
b1 = timeit.default_timer()
print(gcd_fast(a, b))
c1 = timeit.default_timer()

# print(b1-a1)
# print(c1-b1)