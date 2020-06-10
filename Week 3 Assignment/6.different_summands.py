# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    total = 0
    increment = 1
    count = 0
    listOfNum = []

    while total + increment <= n:
        total += increment
        listOfNum.append(increment)
        increment += 1
        count += 1

    listOfNum[count-1] += n - total

    for i in listOfNum:
        summands.append(i)

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
