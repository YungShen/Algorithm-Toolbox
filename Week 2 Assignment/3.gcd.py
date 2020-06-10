# Uses python3
import sys

def gcd_naive(a, b):
    if(a<b):
        return gcd_naive(b,a)
    elif(b==0):
        return a
    else:
        return gcd_naive(a%b,b)


  

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
