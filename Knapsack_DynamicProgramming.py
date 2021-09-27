"""
Knapsack without Repetitions (Dynamic Programming)
==================================================

@author: mhtehrani
September 17, 2021
https://github.com/mhtehrani

"""

def optimal_weight(W, w):
    value = [0]*(len(w)+1)
    for i in range(len(w)+1):
        value[i] = [0]*(W+1)
    #end
    
    for i in range(1,len(w)+1):
        for j in range(1,W+1):
            value[i][j] = value[i-1][j]
            # print(w[i-1], j)
            if w[i-1] <= j:
                val = value[i-1][j-w[i-1]]+w[i-1]
                if value[i][j] < val:
                    value[i][j] = val
                #end
            #end
        #end
    #end
    
    return value[len(w)][W]


W, n = list(map(int, input().split()))
w = list(map(int, input().split()))

print(optimal_weight(W, w))