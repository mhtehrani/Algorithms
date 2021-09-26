"""
Fractional Knapsack
===================

@author: mhtehrani
July 9, 2021
https://github.com/mhtehrani

"""

import numpy

def get_optimal_value_fast(capacity, weights, values):
    value = 0.
    # calculate value per unit weight
    value_per_weight = numpy.divide(values,weights)
    # calculate indices of the maximum value per weight
    indices = numpy.ndarray.tolist(numpy.argsort(numpy.array(value_per_weight))[::-1])
    
    # filling the knapsack
    Empty_space = capacity
    while Empty_space > 0:
        for i in range(len(indices)):
            if Empty_space > 0:
                value += min(Empty_space,weights[indices[i]])*value_per_weight[indices[i]]
                Empty_space += - min(Empty_space,weights[indices[i]])
        
        Empty_space = 0

    return value


n, capacity = map(int, input().split())
values = [0]*n
weights = [0]*n
for i in range(n):
    values[i], weights[i] = map(int, input().split())


opt_value = get_optimal_value_fast(capacity, weights, values)
print("{:.10f}".format(opt_value))
