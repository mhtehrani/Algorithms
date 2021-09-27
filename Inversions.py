"""
Number of Inversions
====================

@author: mhtehrani
July 23, 2021
https://github.com/mhtehrani

"""

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
