"""
Points and Segments
===================

@author: mhtehrani
August 04, 2021
https://github.com/mhtehrani

"""
# import numpy as np
# import random
# import timeit

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(ends)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
            #end
        #end
    #end
    return cnt
#end

def fast_count_segments(s,p,starts,ends,points):
    a = [0]*(s*2+p)
    for i in range(s):
        a[2*i] = [starts[i],0]
        a[2*i+1] = [ends[i],2]
    #end
    for i in range(p):
        a[2*s+i] = [points[i],1,i]
    #end
    
    a.sort()
    # print(a)
    k = [0]*p
    curser = 0
    for i in range(s*2+p):
        if a[i][1] == 0:
            curser += 1
        elif a[i][1] == 2:
            curser += -1
        elif a[i][1] == 1:
            k[a[i][2]] = curser
        #end
    #end
    return k
#end




s, p = map(int, input().split())
starts = [None]*s
ends = [None]*s
for i in range(s):
    starts[i], ends[i] = map(int, input().split())
#end
points = list(map(int, input().split()))

cnt = fast_count_segments(s,p,starts, ends, points)
print(' '.join(map(str, cnt)))

# s, p = 4, 4
# starts = [0,-3,7,2]
# ends = [5,2,10,4]
# points = [1,6,0,2]



# s, p = 2, 3
# starts = [0,7]
# ends = [5,10]
# points = [1,6,11]

# s, p = 1, 3
# starts = [-10]
# ends = [10]
# points = [-100,100,0]

# s = 5
# p = 5
# starts = [5, -3, 0, 3, 3]
# ends = [5, -2, 4, 3, 5]
# points = [1, -3, 3, 6, 7]

# cnt = naive_count_segments(starts, ends, points)
# cnt2 = fast_count_segments(s,p,starts, ends, points)

# print(' '.join(map(str, cnt)))
# for x in cnt:
#     print(x, end=' ')


# print(' '.join(map(str, cnt)))
# for x in cnt:
#     print(x, end=' ')

# while True:
#     s = 50000
#     p = 50000
#     starts = []
#     ends = []
#     points = []
#     for i in range(s):
#         starts.append(random.randint(-500,500))
#         ends.append(random.randint(starts[i],500))
#     #end
#     for i in range(p):
#         points.append(random.randint(-6,6))
#     #end
#     ss = starts[:]
#     ee = ends[:]
#     pp = points[:]
    
#     a1 = timeit.default_timer()
#     b = naive_count_segments(ss, ee, pp)
#     a2 = timeit.default_timer()
#     c = tessst(s,p,starts, ends, points)
#     # print(' '.join(map(str, c)))
#     a3 = timeit.default_timer()
    
#     print(a2-a1)
#     print(a3-a2)
    
#     if b != c:
#         print(b)
#         print(c)
#         break
    
#     print("OK")