# Uses python3
import sys
def calc_fib(n):
    fib_nums=[0,1]
    while(n>len(fib_nums)-1):
        i=len(fib_nums)
        temp_fib=(fib_nums[i-1]+fib_nums[i-2])%10
        fib_nums.append(temp_fib)
    return fib_nums

def fibonacci_sum_naive(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        fib_nums=calc_fib(n)
        sum=0
        for i in fib_nums:
            sum=(sum+i)%10
        return sum



if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n%60))
