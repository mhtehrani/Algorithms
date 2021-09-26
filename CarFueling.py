"""
Car Fueling
===========

@author: mhtehrani
July 9, 2021
https://github.com/mhtehrani

"""

def compute_min_refills(tank, stops):
    # check to see if reaching to destination is possible
    for i in range(len(stops)-1):
        if stops[i+1]-stops[i] > tank:
            return -1
        
    # finding the farthest possible stop
    current_stop = 0
    num_refil = 0
    
    i = 0
    while i < len(stops):
        if stops[i]-stops[current_stop] > tank:
            current_stop = i-1
            num_refil += 1
        else:
            i += 1
    
    return num_refil

distance = int(input())
tank = int(input())
n = int(input())
stops = [0] + list(map(int, input().split())) + [distance]

print(compute_min_refills(tank, stops))