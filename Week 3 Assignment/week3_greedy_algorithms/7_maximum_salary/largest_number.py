#Uses python3

import sys

def largest_number(a):
    #write your code here
    str1=""
    a.sort(reverse=True)
    for i in a:
        a = str(i)
        str1+=a
    return str1

print(largest_number([9,3,5]))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
