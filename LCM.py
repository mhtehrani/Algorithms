"""
Last Digit of a Large Fibonacci Number
======================================

@author: mhtehrani
July 1, 2021
https://github.com/mhtehrani

"""
# Uses python3
# import timeit

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

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

# a1 = timeit.default_timer()
# print(lcm_naive(a, b))
# b1 = timeit.default_timer()
print(lcm_fast(a, b))
# c1 = timeit.default_timer()

# print(b1-a1)
# print(c1-b1)