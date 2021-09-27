"""
Maximum Number of Prizes
========================

@author: mhtehrani
July 14, 2021
https://github.com/mhtehrani

"""

def optimal_summands(n):
    summands = []
    
    check = True
        
    while check:
        if n > len(summands):
            for i in range(len(summands)):
                summands[i] += 1
                n -= 1
            summands.append(1)
            n -= 1
            
        
        elif n == len(summands):
            for i in range(len(summands)):
                summands[i] += 1
                n -= 1
        else:
            summands[0] += n
            n -= n
        
        if n==0:
            check = False
            
    summands.sort()
    return summands


def optimal_summands_fast(n):
    k = int((-1+(1+4*2*n)**0.5)/2)
    summands = []
    for i in range(k):
        summands.append(i+1)
        
    summands[len(summands)-1] += int(n - (k*(k+1))/2)

    return summands


n = int(input())

# summands = optimal_summands(n)
# print(len(summands))
# for x in summands:
#     print(x, end=' ')


summands_final = optimal_summands_fast(n)
print(len(summands_final))
for x in summands_final:
    print(x, end=' ')