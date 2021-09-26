"""
Last Digit of a Large Fibonacci Number
======================================

@author: mhtehrani
July 2, 2021
https://github.com/mhtehrani

"""
# Uses python3
# import timeit

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum_fast(n):
    period = 60
    
    def sum_n(n):
        if n <= 1:
            return n
    
        previous = 0
        current  = 1
        sum      = 1

        for _ in range(n - 1):
            previous, current = current, previous + current
            sum += current
        return sum
    
    if n <= 1:
        return n
    
    if n <= period:
        return sum_n(n) % 10
    
    if n > period:
        return int(n/period)*(sum_n(period) % 10) + (sum_n(n-period*int(n/period)) % 10)


n = int(input())

# a1 = timeit.default_timer()
# print(fibonacci_sum_naive(n))
# b1 = timeit.default_timer()
print(fibonacci_sum_fast(n))
# c1 = timeit.default_timer()

# print(b1-a1)
# print(c1-b1)

