# Uses python3
import sys

def binary_search(a, x):
    low = 0
    mid = len(a) // 2
    upper = len(a)

    if len(a) == 1:
        if a[0] == x:
            
            return a[0]
        else:
            return -1
    if x == a[mid]:
        
        return mid
    else:
        if mid > low:
            arrayl = a[0:mid]
            binary_search(arrayl, x)

        if upper > mid:
            arrayu = a[mid:len(a)]
            binary_search(arrayu, x)
a=[1,2,3,4,5]
b=[1,2,3,4,5]
for x in b:
    print(binary_search(a,x),end=" ")

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(linear_search(a, x), end = ' ')
