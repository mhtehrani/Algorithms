"""
Partitioning (Dynamic Programming)
==================================

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
            
            if w[i-1] <= j:
                val = value[i-1][j-w[i-1]]+w[i-1]
                if value[i][j] < val:
                    value[i][j] = val
                #end
            #end
        #end
    #end
    
    possible = 0
    for i in range(1,len(w)+1):
        if value[i][int(W/3)] == int(W/3):
            for j in range(1,len(w)+1):
                if value[j][int(2*W/3)] == int(2*W/3):
                    possible = 1
                    return possible
                #end
            #end
        #end
    #end
    
    return possible


n = int(input())
w = list(map(int, input().split()))

W = 0
for i in range(n):
    W += w[i]
#end

if n < 3:
    print(0)
elif W % 3 != 0:
    print(0)
else:
    print(optimal_weight(W, w))
#end
