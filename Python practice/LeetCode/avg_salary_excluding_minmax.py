# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

def calc(arr):
    sum = 0
    minimum = arr[0]
    maximum = arr[0]
    for val in arr:
        minimum = min(minimum, val)
        maximum = max(maximum, val)
        sum += val
    return (sum - minimum - maximum)/(len(arr) - 2)

print(calc([4000,3000,1000,2000]))

print(calc([1000,2000,3000]))

print(calc( [6000,5000,4000,3000,2000,1000]))

print(calc([8000,9000,2000,3000,6000,1000]))