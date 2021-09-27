"""
Number of Inversions
====================

@author: mhtehrani
July 23, 2021
https://github.com/mhtehrani

"""
# Uses python3
# import random
# import timeit

def number_of_inversions_naive(a):
    number_of_inversions = 0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                number_of_inversions += 1
    
    return number_of_inversions

def inversions3(a):
    left = 0
    right = len(a)-1
    b = []
    number_of_inversions = 0
    if right - left == 1:
        if a[left] > a[right]:
            number_of_inversions += 1
            b.append(a[right])
            b.append(a[left])
        else:
            b.append(a[left])
            b.append(a[right])
        #end
        return b, number_of_inversions
    elif right - left < 1:
        b.append(a[left])
        return b, number_of_inversions
    #end
    ave = (left + right) // 2
    a_left, number_of_inversions_left = inversions3(a[left:ave+1])
    a_right, number_of_inversions_right = inversions3(a[ave+1:right+1])
    number_of_inversions = number_of_inversions_left + number_of_inversions_right
    n_left, n_right = ave+1 - left, right-ave
    i, j = 0, 0
    for k in range(n_left+n_right):
        if a_left[i] <= a_right[j]:
            b.append(a_left[i])
            i += 1
            if i >= n_left:
                b = b+ a_right[j:n_right]
                break
            #end
        else:
            b.append(a_right[j])
            j += 1
            number_of_inversions += n_left - i
            if j >= n_right:
                b = b +a_left[i:n_left]
                break
            #end
        #end
    #end
    return b, number_of_inversions

n = int(input())
a = list(map(int, input().split()))
a, n = inversions3(a)
print(n)

# # a = [0,1,2,3,4,5]
# # a = [5,4,3,2,1,0]
# a = [2, 7, 2, 3, 4]
# print(number_of_inversions_naive(a))
# a, n = inversions3(a)
# print(n)

# while True:
#     a = []
#     n = random.randint(10000,10000)
#     for i in range(n):
#         a.append(random.randint(1, 100))
    
#     a1 = timeit.default_timer()
#     b = number_of_inversions_naive(a)
#     a2 = timeit.default_timer()
#     c_, c = inversions3(a)
#     a3 = timeit.default_timer()
    
#     print(a2-a1)
#     print(a3-a2)
    
#     if b != c:
#         print(b)
#         print(c)
#         print(a)
#         break
    
#     print("OK")