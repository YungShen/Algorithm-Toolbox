# Uses python3
import sys

def get_majority_element(a, left, right):
    size=len(a)
    m = {} 
    for i in range(size): 
        if a[i] in m: 
            m[a[i]] += 1
        else: 
            m[a[i]] = 1
    count = 0
    for key in m: 
        if m[key] > size / 2: 
            count = 1
            return 1
            break
    if(count == 0): 
        return -1







if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
