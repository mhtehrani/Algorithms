"""
Points and Segments
===================

@author: mhtehrani
August 04, 2021
https://github.com/mhtehrani

"""

def fast_count_segments(s,p,starts,ends,points):
    a = [0]*(s*2+p)
    for i in range(s):
        a[2*i] = [starts[i],0]
        a[2*i+1] = [ends[i],2]
    
    for i in range(p):
        a[2*s+i] = [points[i],1,i]
    
    
    a.sort()
    
    k = [0]*p
    curser = 0
    for i in range(s*2+p):
        if a[i][1] == 0:
            curser += 1
        elif a[i][1] == 2:
            curser += -1
        elif a[i][1] == 1:
            k[a[i][2]] = curser
        
    
    return k


s, p = map(int, input().split())
starts = [None]*s
ends = [None]*s
for i in range(s):
    starts[i], ends[i] = map(int, input().split())

points = list(map(int, input().split()))

cnt = fast_count_segments(s,p,starts, ends, points)

print(' '.join(map(str, cnt)))
