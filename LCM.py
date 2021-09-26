"""
Least Common Multiple
=====================

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

def lcm_fast(a, b):
    return int(a*b/gcd_fast(a, b))


a, b = map(int, input().split())

print(lcm_fast(a, b))
