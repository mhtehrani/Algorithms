"""
Majority Element
================

@author: mhtehrani
July 20, 2021
https://github.com/mhtehrani

"""

def get_majority_element_fast(a):
    if len(a) == 1:
        return 1
    
    a.sort()
    mid = int(len(a)/2)
    if a.count(a[mid]) > mid:
        return 1
    else:
        return 0
    

def get_majority_element_fast2(a):
    if len(a) == 1:
        return 1
    
    a.sort()
    mid = int((len(a)-1)/2)
    for i in range(mid+1,len(a)):
        if a[i] != a[mid]:
            i = i-1
            break
        
    
    if a[i-int(len(a)/2)] == a[mid]:
        return 1
    
    return 0

n = int(input())
a = list(map(int, input().split()))

# a = [2, 3];
fast = get_majority_element_fast(a)
# fast2 = get_majority_element_fast2(a)

# print(get_majority_element_fast(a))

# stress check

# while True:
#     a = []
#     n = random.randint(1, 10)
#     for i in range(n):
#         a.append(random.randint(1, 10))
    
#     fast = get_majority_element_fast(a)
#     fast2 = get_majority_element_fast2(a)
    
#     print(fast, fast2)
    
#     if fast != fast2:
#         print(a)
#         break
