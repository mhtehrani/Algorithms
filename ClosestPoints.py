"""
Closet Points
=============

@author: mhtehrani
August 05, 2021
https://github.com/mhtehrani

"""

import math

def minimum_distance_fast(n, Points,delta):
    if n == 2:
        return math.sqrt((Points[1][0]-Points[0][0])**2+(Points[1][1]-Points[0][1])**2)
    elif n <= 1:
        return delta
    
    Px = Points[:]
    
    half_point = int(n/2)
    for i in range(half_point,0,-1):
        if Px[i][0] < Px[half_point][0]:
            half_point = i+1
            break
        
    
    dis1 = minimum_distance_fast(half_point, Px[0:half_point],delta)
    dis2 = minimum_distance_fast(n-half_point, Px[half_point:n],delta)
    
    delta = min(dis1,dis2)
    Lower_B = 0
    for i in range(half_point,0,-1):
        if Px[i][0] <= Px[half_point][0]-delta:
            Lower_B = i+1
            break
        
    
    Upper_B = n
    for i in range(half_point,n):
        if Px[i][0] >= Px[half_point][0]+delta:
            Upper_B = i
            break
        
    
    
    Set = Px[Lower_B:Upper_B]
    Set.sort(key=lambda x: x[1])
    for i in range(Upper_B-Lower_B):
        for j in range(i+1,min(i+7,Upper_B-Lower_B)):
            dist = math.sqrt((Set[j][0]-Set[i][0])**2+(Set[j][1]-Set[i][1])**2)
            if dist < delta:
                delta = dist
            
        
    
    
    return delta





n = int(input())
Points = [None]*n
for i in range(n):
    xx, yy = map(int, input().split())
    Points[i] = [xx,yy]

Points.sort()
delta = math.sqrt((Points[1][0]-Points[0][0])**2+(Points[1][1]-Points[0][1])**2)

print("{0:.9f}".format(minimum_distance_fast(n, Points, delta)))
