"""
Maximum Pairwise Product
========================

@author: mhtehrani
May 4, 2021
https://github.com/mhtehrani

"""


def max_pairwise_product(numbers):
    i1 = numbers.index(max(numbers))
    max1 = numbers[i1]
    temp = numbers[0:i1]+numbers[i1+1:]
    i2 = temp.index(max(temp))
    max2 = temp[i2]
    return max1*max2

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    
    print(max_pairwise_product(input_numbers))
