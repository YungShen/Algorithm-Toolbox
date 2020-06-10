# Uses python3
import sys
def gcd_naive(a, b):
    if(a<b):
        return gcd_naive(b,a)
    elif(b==0):
        return a
    else:
        return gcd_naive(a%b,b)

def lcm_naive(a, b):
    gcd=gcd_naive(a,b)
    a_remainder=a/gcd
    b_remainder=b/gcd
    return int(gcd*a_remainder*b_remainder)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

