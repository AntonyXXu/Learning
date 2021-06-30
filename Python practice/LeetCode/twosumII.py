def twoSum(numbers, target):
    i = 0
    j = len(numbers)-1
    while i < j:
        print(i, j)
        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]
        if numbers[i] + numbers[j] > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]


print(twoSum(numbers = [-1,0], target = -1))
print(twoSum(numbers = [2,3,4], target = 6))
print(twoSum(numbers = [2,7,11,15], target = 9))