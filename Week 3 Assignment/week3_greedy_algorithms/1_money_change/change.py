# Uses python3
import sys

def get_change(m):
    #write your code here
    num=0
    while(m>0):
        if(m>10):
            m=m-10
            num+=1
        elif(m>5):
            m=m-5
            num+=1
        else:
            m=m-1
            num+=1
    
    return num
print(get_change(28))
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
