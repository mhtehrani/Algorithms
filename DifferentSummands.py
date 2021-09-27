"""
Maximum Number of Prizes
========================

@author: mhtehrani
July 14, 2021
https://github.com/mhtehrani

"""

def optimal_summands_fast(n):
    k = int((-1+(1+4*2*n)**0.5)/2)
    summands = []
    for i in range(k):
        summands.append(i+1)
        
    summands[len(summands)-1] += int(n - (k*(k+1))/2)

    return summands


n = int(input())

summands_final = optimal_summands_fast(n)
print(len(summands_final))
for x in summands_final:
    print(x, end=' ')
