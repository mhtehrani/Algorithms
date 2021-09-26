"""
Fibonacci Number mode 𝑚
========================

@author: mhtehrani
July 2, 2021
https://github.com/mhtehrani

"""

def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
        = current, (previous + current) % m
         
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

def calc_fib_fast(n):
    f = [0]
    f.append(1)
    if (n <= 1):
        return f[n]
    else:
        for i in range(2,n+1):
            f.append(f[i-1]+f[i-2])
        return f[n]

def get_fibonacci_huge_fast(n, m):
    mode_length = pisanoPeriod(m)
    n_new = n % mode_length
    return calc_fib_fast(n_new) % m

n, m = map(int, input().split())

print(get_fibonacci_huge_fast(n, m))
