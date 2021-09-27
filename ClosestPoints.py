"""
Closet Points
=============

@author: mhtehrani
August 05, 2021
https://github.com/mhtehrani

"""
#Uses python3
import math
# import numpy as np
# import random
# import timeit

def minimum_distance_naive(n, Points):
    best_dist = math.sqrt((Points[1][0]-Points[0][0])**2+(Points[1][1]-Points[0][1])**2)
    for i in range(n):
        for j in range(i+1,n):
            dist = math.sqrt((Points[j][0]-Points[i][0])**2+(Points[j][1]-Points[i][1])**2)
            if dist < best_dist:
                best_dist = dist
            #end
        #end
    #end
    return best_dist
#end

def minimum_distance_fast(n, Points,delta):
    if n == 2:
        return math.sqrt((Points[1][0]-Points[0][0])**2+(Points[1][1]-Points[0][1])**2)
    elif n <= 1:
        return delta
    #end
    Px = Points[:]
    # Py = Points[:]
    # Py.sort(key=lambda x: x[1])
    
    half_point = int(n/2)
    for i in range(half_point,0,-1):
        if Px[i][0] < Px[half_point][0]:
            half_point = i+1
            break
        #end
    #end
    dis1 = minimum_distance_fast(half_point, Px[0:half_point],delta)
    dis2 = minimum_distance_fast(n-half_point, Px[half_point:n],delta)
    
    delta = min(dis1,dis2)
    Lower_B = 0
    for i in range(half_point,0,-1):
        if Px[i][0] <= Px[half_point][0]-delta:
            Lower_B = i+1
            break
        #end
    #end
    
    Upper_B = n
    for i in range(half_point,n):
        if Px[i][0] >= Px[half_point][0]+delta:
            Upper_B = i
            break
        #end
    #end
    
    Set = Px[Lower_B:Upper_B]
    Set.sort(key=lambda x: x[1])
    for i in range(Upper_B-Lower_B):
        for j in range(i+1,min(i+7,Upper_B-Lower_B)):
            dist = math.sqrt((Set[j][0]-Set[i][0])**2+(Set[j][1]-Set[i][1])**2)
            if dist < delta:
                delta = dist
            #end
        #end
    #end
    
    return delta
#end




n = int(input())
Points = [None]*n
for i in range(n):
    xx, yy = map(int, input().split())
    Points[i] = [xx,yy]
#end

# n = 4
# Points = [[7,7],[1,100],[4,8],[7,7]]

# n= 11
# Points = [[4,4],[-2,-2],[-3,-4],[-1,3],[2,3],[-4,0],[1,1],[-1,-1],[3,-1],[-4,2],[-2,4]]



Points.sort()
delta = math.sqrt((Points[1][0]-Points[0][0])**2+(Points[1][1]-Points[0][1])**2)
# jjjjj = minimum_distance_fast(n, Points, delta)

print("{0:.9f}".format(minimum_distance_fast(n, Points, delta)))



# while True:
#     n = 100000
#     Points = [None]*n
#     for i in range(n):
#         Points[i] = [random.randint(-10000,10000),random.randint(-10000,10000)]
#     #end
#     Points.sort()
#     delta = math.sqrt((Points[1][0]-Points[0][0])**2+(Points[1][1]-Points[0][1])**2)
    
    # a1 = timeit.default_timer()
    # b = minimum_distance_naive(n, Points)
    # a2 = timeit.default_timer()
    # c = minimum_distance_fast(n, Points, delta)
    # print(' '.join(map(str, c)))
    # a3 = timeit.default_timer()
    
    # print(a2-a1)
    # print(a3-a2)
    
    # if b != c:
    #     print(b)
    #     print(c)
    #     break
    
    # print("OK")