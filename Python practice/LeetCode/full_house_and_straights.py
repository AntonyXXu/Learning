# Question1:
# Input is a list of values, check you can create sets of full houses (3x 1, 2x 2) using ALL numbers

#Question2:
# Input is a list of values, check if you can create sets of straights of 5

#Return a boolean value

#Question3:
# Given a list of values, can you N-ary straights

# Straight can be any >=3
# Between 1 - 100

# ex3) [3, 4, 5, 6] works, [3, 4, 5, 5, 6] doesn't work 

import collections
#Q1:
def fullHouse(nums):
    if not nums or len(nums) % 5 != 0:
        return False
    d = collections.defaultdict(int)
    for num in nums:
        d[num] += 1
    threes = 0
    twos = 0
    sixes = 0
    for count in d.values():
        if count % 5 == 0:
            continue
        elif count % 3 == 0 and count % 2 != 0:
            threes += count // 3
        elif count % 2 == 0 and count % 3 != 0:
            twos += count // 2
        elif count % 6:
            sixes += count % 6
        else:
            return False
    if twos == threes:
        return sixes % 2 == 0

    elif twos > threes:
        twos = twos - threes
        threes = 0
    else:
        threes = threes - twos
        twos = 0
    if not sixes:
        return False
    
    
    while twos >= 0:
        twos -= 3


    if twos or sixes or threes:
        return False
    return True

def straight(nums):
    if not nums or len(nums) % 5 != 0:
        return False
    d = collections.Counter()
    for num in nums:
        d[num] += 1
    for key in sorted(d.keys()):
        while d[key]:
            for i in range(key, key + 5):
                if not d[i]:
                    return False
                d[i] -= 1
    return True

print(straight([1,2,3,4,5,2,3,4,5,6]))
print(straight([1,1,2,2,3,3,4,4,5,5]))
print(straight([3,3,2,2,1,4,5,4,1,5]))
print(straight([1,2,3,4,5,2,3,4,4,5]))

