"""
Maximum Value of an Arithmetic Expression (Dynamic Programming)
===============================================================

@author: mhtehrani
September 17, 2021
https://github.com/mhtehrani

"""

import numpy

def eval(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(d,op):
    n = len(d)
    m = numpy.empty((n,n))
    m[:] = numpy.NaN
    for i in range(n):
        m[i,i] = d[i]
    #end
    
    M = m.copy()
    
    for s in range(1,n):
        for i in range(n-s):
            j = i+s
            min_ = float("inf")
            max_ = -float("inf")

            for k in range(i,j):
                a1 = eval(M[i][k],op[k],M[k+1][j])
                a2 = eval(m[i][k],op[k],M[k+1][j])
                a3 = eval(M[i][k],op[k],m[k+1][j])
                a4 = eval(m[i][k],op[k],m[k+1][j])
                
                min_ = min(min_, a1, a2, a3, a4)
                max_ = max(max_, a1, a2, a3, a4)
            #end
            
            m[i,j] = min_
            M[i,j] = max_
        #end
    #end
    
    return int(M[0,n-1])

   
string = input()
n = int((len(string)+1)/2)

d = []
d.append(int(string[0]))
op = []
for i in range(1,n):
    d.append(int(string[2*i]))
    op.append(string[2*i-1])
#end

print(get_maximum_value(d,op))