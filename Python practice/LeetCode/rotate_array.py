# https://leetcode.com/problems/rotate-array/

def rotate(nums, k):
    k = k % len(nums)

    changed = 0
    i = 0
    while changed < len(nums):
        prev = nums[i]
        j = (i + k) % len(nums)
        while j != i:
            temp = nums[j]
            nums[j] = prev
            prev = temp
            j = (j + k) % len(nums)
            changed += 1
        temp = nums[j]
        nums[j] = prev
        prev = temp
        j = (j + k) % len(nums)
        changed += 1
        i += 1

    print(nums)


rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
rotate(nums=[-1, -100, 3, 99], k=2)
