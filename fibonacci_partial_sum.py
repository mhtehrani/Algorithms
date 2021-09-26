"""
Last Digit of a Large Fibonacci Number
======================================

@author: mhtehrani
July 2, 2021
https://github.com/mhtehrani

"""

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


def fibonacci_partial_sum_fast(from_, to):
    if from_ == 0:
        sum_from = 0
    else:
        sum_from = fibonacci_sum_fast(from_-1)
    
    sum_to = fibonacci_sum_fast(to)
    
    if sum_to >= sum_from:
        return sum_to - sum_from
    else:
        return (sum_to + 10) - sum_from

from_, to = map(int, input().split())

print(fibonacci_partial_sum_fast(from_, to))
