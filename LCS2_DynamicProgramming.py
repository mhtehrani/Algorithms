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
    # =========================================================================
    LCSs = [None]*(len(row)+1)
    for i in range(len(row)+1):
        LCSs[i] = [0]*(len(col)+1)
    #end
    
    # Filling the Sequence and LCS tables
    # =========================================================================
    for i in range(1,len(row)+1):
        for j in range(1,len(col)+1):
            # print(row[i-1] , col[j-1])
            
            # Seq[i][j] = Seq[i-1][j].copy()
            # for k in Seq[i][j-1]:
            #     Seq[i][j].append(k.copy())
            # #end
            
            # if they match
            if row[i-1] == col[j-1]:
                LCSs[i][j] = LCSs[i-1][j-1] +1
                # if len(Seq[i-1][j-1]) == 0:
                #     Seq[i][j].append([row[i-1]])
                # else:
                #     for k in range(len(Seq[i-1][j-1])):
                #         temp = Seq[i-1][j-1][k].copy()
                #         temp.append(row[i-1])
                #         Seq[i][j].append(temp)
                #     #end
                # #end
            
            # if they don't match
            else:
                LCSs[i][j] = max(LCSs[i-1][j], LCSs[i][j-1])
            #end
            
            # print(Seq)
        #end
    #end
    
    return LCSs[len(row)][len(col)]#, Seq[len(row)][len(col)]


def LCS(row, col):
    # Creating empty table of sequence
    # =========================================================================
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
    # =========================================================================
    LCSs = [None]*(len(row)+1)
    for i in range(len(row)+1):
        LCSs[i] = [0]*(len(col)+1)
    #end
        
    # Filling the Sequence and LCS tables
    # =========================================================================
    for i in range(1,len(row)+1):
        for j in range(1,len(col)+1):
            print(row[i-1] , col[j-1])
            # if they match
            if row[i-1] == col[j-1]:
                if len(Seq[i-1][j-1]) == 0:
                    Seq[i][j].append([row[i-1]])
                    LCSs[i][j] = 1
                else:
                    for k in range(len(Seq[i-1][j-1])):
                        temp = Seq[i-1][j-1][k].copy()
                        temp.append(row[i-1])
                        Seq[i][j].append(temp)
                        if len(Seq[i][j][k]) > LCSs[i][j]:
                            LCSs[i][j] = len(Seq[i][j][k])
                    #end
                #end
            
            # if they don't match
            else:
                if LCSs[i-1][j] > LCSs[i][j-1]:
                    Seq[i][j] = Seq[i-1][j].copy()
                    LCSs[i][j] = LCSs[i-1][j]
                elif LCSs[i-1][j] < LCSs[i][j-1]:
                    Seq[i][j] = Seq[i][j-1].copy()
                    LCSs[i][j] = LCSs[i][j-1]
                else:
                    Seq[i][j] = Seq[i-1][j].copy()
                    LCSs[i][j] = LCSs[i-1][j]
                    for k in range(len(Seq[i][j-1])):
                        if Seq[i][j-1][k] not in Seq[i][j]:
                            Seq[i][j].append(Seq[i][j-1][k].copy())
                        #end
                    #end
                #end
            #end
        #end
    #end
    
    return LCSs[len(row)][len(col)]#, Seq[len(row)][len(col)]



n = int(input())
row = list(map(int, input().split()))


m = int(input())
col = list(map(int, input().split()))


# n = 3
# row = [3,3,1]
# m = 3
# col = [1,3,3]


print(LCS_fast(row, col))


