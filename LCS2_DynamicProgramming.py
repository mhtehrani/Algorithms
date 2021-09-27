"""
Longest Common Subsequence of Two Sequences (Dynamic Programming)
=================================================================

@author: mhtehrani
September 12, 2021
https://github.com/mhtehrani

"""

def LCS_fast(row, col):
    Seq = [None]*(len(row)+1)
    for i in range(len(row)+1):
        Seq[i] = [None]*(len(col)+1)
    #end
    
    for i in range(len(row)+1):
        for j in range(len(col)+1):
            Seq[i][j] = []
        #end
    #end
    
    # Creating empty table of LCSs and initializing the 1st row and column with 0
    # ===========================================================================
    LCSs = [None]*(len(row)+1)
    for i in range(len(row)+1):
        LCSs[i] = [0]*(len(col)+1)
    #end
    
    # Filling the Sequence and LCS tables
    # =========================================================================
    for i in range(1,len(row)+1):
        for j in range(1,len(col)+1):
            
            # if they match
            if row[i-1] == col[j-1]:
                LCSs[i][j] = LCSs[i-1][j-1] +1
            
            # if they don't match
            else:
                LCSs[i][j] = max(LCSs[i-1][j], LCSs[i][j-1])
            #end
        #end
    #end
    
    return LCSs[len(row)][len(col)]#, Seq[len(row)][len(col)]


n = int(input())
row = list(map(int, input().split()))


m = int(input())
col = list(map(int, input().split()))

print(LCS_fast(row, col))
