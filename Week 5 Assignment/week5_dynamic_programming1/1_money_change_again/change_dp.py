# Uses python3
import sys

def get_change(S,n):
    #write your code here
    
    if n == 0:
        return 0
    if n < 0:
        return sys.maxsize
 
    minCost = sys.maxsize
    for i in range(len(S)):
        cost = get_change(S, n - S[i]) + 1
        minCost = min(minCost, cost)
    return minCost

print(get_change([1,3,5,7],18))

if __name__ == '__main__':
    m = int(sys.stdin.read())
    s=[1,3,4]
    print(get_change(m,s))
