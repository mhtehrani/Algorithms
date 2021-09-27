"""
Longest Common Subsequence of Three Sequences (Dynamic Programming)
===================================================================

@author: mhtehrani
September 15, 2021
https://github.com/mhtehrani

"""

def LCS3_fast(row, col, dep):
    # Creating empty table of sequence
    Seq = [None]*(len(row)+1)
    for i in range(len(row)+1):
        Seq[i] = [None]*(len(col)+1)
        for j in range(len(col)+1):
            Seq[i][j] = [None]*(len(dep)+1)
        #end
    #end
    
    for i in range(len(row)+1):
        for j in range(len(col)+1):
            for k in range(len(dep)+1):
                Seq[i][j][k] = []
            #end
        #end
    #end
    
    # Creating empty table of LCSs and initializing the 1st row and column with 0
    # ===========================================================================
    LCSs = [None]*(len(row)+1)
    for i in range(len(row)+1):
        LCSs[i] = [None]*(len(col)+1)
        for j in range(len(col)+1):
            LCSs[i][j] = [0]*(len(dep)+1)
        #end
    #end
    
    # Filling the Sequence and LCS tables
    # ===================================
    for i in range(1,len(row)+1):
        for j in range(1,len(col)+1):
            for k in range(1,len(dep)+1):
                # if they match
                if row[i-1] == col[j-1]== dep[k-1]:
                    LCSs[i][j][k] = LCSs[i-1][j-1][k-1] +1
                
                # if they don't match
                else:
                    LCSs[i][j][k] = max(LCSs[i-1][j][k], LCSs[i][j-1][k], LCSs[i][j][k-1])
                #end
            #end
        #end
    #end
    
    return LCSs[len(row)][len(col)][len(dep)]


n = int(input())
row = list(map(int, input().split()))


m = int(input())
col = list(map(int, input().split()))

l = int(input())
dep = list(map(int, input().split()))

print(LCS3_fast(row, col, dep))
