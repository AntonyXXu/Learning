# https://leetcode.com/problems/majority-element-ii/

def maj(nums):
    counter1 = 0
    counter2 = 0
    num1 = None
    num2 = None
    for num in nums:
        if num == num1:
            counter1 += 1
        elif num == num2:
            counter2 += 1
        elif counter1 == 0:
            num1 = num
            counter1 += 1
        elif counter2 == 0:
            num2 = num
            counter2 += 1
        else:
            counter1 -= 1
            counter2 -= 1
    res = []
    if nums.count(num1) * 3 > len(nums):
        res.append(num1)
    if nums.count(num2) * 3 > len(nums):
        res.append(num2)
    return res


print(maj([3, 2, 3]))
print(maj([1, 2]))
print(maj([1]))
print(maj([2, 2]))
