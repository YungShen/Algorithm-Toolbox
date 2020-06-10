# Uses python3
import sys
def get_value(capacity,weights,values,valueperunits):
       
        max_index=valueperunits.index(max(valueperunits))
        if(capacity<weights[max_index]):
            return valueperunits[max_index]*capacity
        else:
            capacity=capacity-weights[max_index]
        
            maxv=valueperunits.pop(max_index)
            weight=weights.pop(max_index)
            values.pop(max_index)
            return maxv*weight+get_value(capacity,weights,values,valueperunits)
            

def get_optimal_value(capacity, weights, values):

    # write your code here
    value=0
    valueperunits=[]
    i=0
    n=len(weights)
    if(n<2):
        if capacity>weights[0]:
            return weights[0]*values[0]
        else:
            return values[0]*capacity
    else:
        while(i<n):
            valueperunit=values[i]/weights[i]
            valueperunits.append(valueperunit)
            i+=1
        value=get_value(capacity,weights,values,valueperunits)
        return value



   


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
