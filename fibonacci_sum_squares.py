"""
Last Digit of a Large Fibonacci Number
======================================

@author: mhtehrani
July 2, 2021
https://github.com/mhtehrani

"""
# Uses python3

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_sum_squares_fast(n):
    period = 60
    
    def sum_n2(n):
        if n <= 1:
            return n
    
        previous = 0
        current  = 1
        sum      = 1

        for _ in range(n - 1):
            previous, current = current, previous + current
            sum += current**2
        return sum
    
    if n <= 1:
        return n
    
    if n <= period:
        return sum_n2(n) % 10
    
    if n > period:
        return int(n/period)*(sum_n2(period) % 10) + (sum_n2(n-period*int(n/period)) % 10)



n = int(input())
# print(fibonacci_sum_squares_naive(n))
print(fibonacci_sum_squares_fast(n))