"""
Primitive Calculator (Dynamic Programming)
==================================

@author: mhtehrani
September 07, 2021
https://github.com/mhtehrani

"""

def Optimal_Sequence(n):
    Value = [None]*(n+1)
    Sequence = [None]*(n+1)
    
    int_Val = [0,0,1,1]
    ini_Seq = [[0],[1],[1,2],[1,3]]
    
    if n <= 3:
        return int_Val[n], ini_Seq[n]
    else:
        Value[0:4] = [0,1,1,1]
        for i in range(4,n+1):
            Value[i] = Value[i-1]+1
            if i % 3 == 0:
                if Value[int(i/3)]+1 < Value[i]:
                    Value[i] = Value[int(i/3)]+1
            
            if i % 2 == 0:
                if Value[int(i/2)]+1 < Value[i]:
                    Value[i] = Value[int(i/2)]+1
            
        
    
    
    Sequence = [None]*(Value[n]+1)
    Sequence[-1] = n
    Sequence[0] = 1
    
    for j in range(Value[n]-1,0,-1):
        n_tem = Sequence[j+1]
        Sequence[j] = Sequence[j+1]-1
        
        if n_tem % 2 == 0:
            if Value[int(n_tem/2)] == Value[Sequence[j+1]]-1:
                Sequence[j] = int(n_tem/2)
            
        
        
        if n_tem % 3 == 0:
            if Value[int(n_tem/3)] == Value[Sequence[j+1]]-1:
                Sequence[j] = int(n_tem/3)
            
        
    return Value[n], Sequence


n = int(input())

O_Value, O_Sequence = Optimal_Sequence(n)
print(O_Value)
print(*O_Sequence, sep=' ')
