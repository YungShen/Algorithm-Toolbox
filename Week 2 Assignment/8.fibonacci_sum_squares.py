# Uses python3
from sys import stdin
def calc_fib(n):
    fib_nums=[0,1]
    if(n<len(fib_nums)):
        return fib_nums[n]
    while(n>len(fib_nums)-1):
        i=len(fib_nums)
        temp_fib=fib_nums[i-1]+fib_nums[i-2]
        fib_nums.append(temp_fib)
    return fib_nums
def fibonacci_sum_squares_naive(n):
    fib_nums=calc_fib(n)
    sum=0
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        for i in fib_nums:
            sum=sum+i**2
            sum=sum%10
        return sum
    


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n%60))
