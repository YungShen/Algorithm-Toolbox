# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    num_refill=0
    cur_loc=0
    i=0
    
    while(cur_loc<distance):
        while( i < len(stops) and tank>stops[i]-cur_loc   ):
            i+=1
        cur_loc=stops[i-1]
        num_refill+=1
        if(tank>distance-cur_loc):
            break
    

    return num_refill
    
print(compute_min_refills(10,3,[1,2,5,9]))

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
