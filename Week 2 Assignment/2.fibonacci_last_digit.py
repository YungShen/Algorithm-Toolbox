# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    fib_nums=[0,1]
    if(n<len(fib_nums)):
        return fib_nums[n]%10
    while(n>len(fib_nums)-1):
        i=len(fib_nums)
        temp_fib=fib_nums[i-1]+fib_nums[i-2]
        temp_fib=temp_fib%10
        fib_nums.append(temp_fib)
    return fib_nums[n]



if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
