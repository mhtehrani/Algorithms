"""
Last Digit of a Large Fibonacci Number
======================================

@author: mhtehrani
July 1, 2021
https://github.com/mhtehrani

"""

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

print(gcd_fast(a, b))
