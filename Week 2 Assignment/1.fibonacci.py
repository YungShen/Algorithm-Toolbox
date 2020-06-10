# Uses python3
def calc_fib(n):
    fib_nums=[0,1]
    if(n<len(fib_nums)):
        return fib_nums[n]
    while(n>len(fib_nums)-1):
        i=len(fib_nums)
        temp_fib=fib_nums[i-1]+fib_nums[i-2]
        fib_nums.append(temp_fib)
    return fib_nums[n]



n = int(input())
print(calc_fib(n))
