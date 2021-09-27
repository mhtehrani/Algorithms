"""
Money Change (Dynamic Programming)
==================================

@author: mhtehrani
September 07, 2021
https://github.com/mhtehrani

"""

def Change(n):
    Value = [None]*(n+1)
    initial = [0,1,2,1,1]
    
    if n<=4:
        return initial[n]
    else:
        Value[0:5] = initial
        for i in range(5,n+1):
            Value[i] = min(Value[i-1]+1,Value[i-3]+1,Value[i-4]+1)
        #end
    #end
    
    return Value[n]

n = int(input())
print(Change(n))


