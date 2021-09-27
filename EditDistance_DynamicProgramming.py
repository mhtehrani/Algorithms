"""
Edit Distance (Dynamic Programming)
===================================

@author: mhtehrani
September 07, 2021
https://github.com/mhtehrani

"""

import numpy


def Edit_Distance(row, column):
    Dis = numpy.zeros([len(row)+1, len(column)+1])
    
    for i in range(1,len(row)+1):
        Dis[i,0] = Dis[i-1,0]+1
    #end
    
    for j in range(1,len(column)+1):
        Dis[0,j] = Dis[0,j-1]+1
    #end
    
    for i in range(1,len(row)+1):
        for j in range(1,len(column)+1):
            if row[i-1] == column[j-1]:
                val = 0
            else:
                val = 1;
            #end
            
            Dis[i,j] = min(Dis[i,j-1]+1,Dis[i-1,j]+1,Dis[i-1,j-1]+val)
        #end
    #end
    
    return int(Dis[len(row),len(column)])

row = input()
column = input()

print(Edit_Distance(row, column))
