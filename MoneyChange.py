"""
Money Change
============

@author: mhtehrani
July 9, 2021
https://github.com/mhtehrani

"""

import math

def get_change_fast(m):
    n_10 = 0
    n_5 = 0
    n_1 = 0
    
    # number of 10 coins
    if m >= 10:
        n_10 = math.floor(m/10)
    
    # number of 5 coins
    if m - n_10*10 >= 5:
        n_5 = math.floor((m - n_10*10)/5)
    
    
    # number of 1 coins
    if m - n_10*10 - n_5*5 >= 1:
        n_1 = m - n_10*10 - n_5*5
        
    return n_10 + n_5 + n_1

m = int(input())

print(get_change_fast(m))