def plusOne(lst):
    carry = 0
    for i in range(len(lst)-1, -1, -1):
        lst[i] += 1
        if lst[i] == 10:
            lst[i] = 0
            carry = 1
        else:
            return lst
    if carry == 1:
        lst.insert(0, 1)
    return lst

print(plusOne([1,2,9]))
print(plusOne([1,2,0]))
print(plusOne([4,3,2,1]))
print(plusOne([0]))
print(plusOne([9,9,9]))
