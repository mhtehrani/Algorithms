"""
Last Digit of a Large Fibonacci Number
======================================

@author: mhtehrani
July 1, 2021
https://github.com/mhtehrani

"""

def get_fibonacci_last_digit_fast(n):
    f = [0]
    f.append(1)
    if (n <= 1):
        return f[n]
    else:
        for i in range(2,n+1):
            f.append( (f[i-1]+f[i-2]) %10)
        return f[n] % 10

n = int(input())
print(get_fibonacci_last_digit_fast(n))