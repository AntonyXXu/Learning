# Question1:
# Input is a list of values, check you can create sets of full houses (3x 1, 2x 1) using ALL numbers

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
    print(d.values())
    for count in d.values():
        if count % 5 == 0:
            continue
        elif count % 3 == 0 and count % 2 != 0:
            threes += count // 3
        elif count % 2 == 0 and count % 3 != 0:
            twos += count // 2
        elif count % 6 == 0:
            sixes += count // 6
        else:
            return False
    # Minimize twos and threes
    if twos == threes:
        return sixes % 2 == 0
    
    print(twos, threes, sixes)
    while sixes > 0:
        if twos > threes:
            twos = twos - threes
            threes = 0
        else:
            threes = threes - twos
            twos = 0
        if twos:
            required = twos // 3 + twos % 3 != 0
            sixes -= required
            threes = required * 2 - twos
            twos -= required * 2
        elif threes:
            required = threes // 2 + threes % 2 != 0
            sixes -= required
            twos = required * 3 - threes
            threes -= required * 3
    if sixes < 0 or twos or threes:
        return False
    return True
print('full house')
print(fullHouse(  [1,1,1,1,2,2,4,4,4,4,4,4,5,5,5]      ))


#Q2
def straight(nums):
    if not nums or len(nums) % 5 != 0:
        return False
    d = collections.Counter()
    for num in nums:
        d[num] += 1
    for key in sorted(d.keys()):
        if d[key]:
            num = d[key]
            for i in range(key, key + 5):
                if d[i] < num:
                    return False
                d[i] -= num
    return True
print('straight')

print(straight([1,2,3,4,5,2,3,4,5,6]))
print(straight([1,1,2,2,3,3,4,4,5,5]))
print(straight([3,3,2,2,1,4,5,4,1,5]))
print(straight([1,2,3,4,5,2,3,4,4,5]))


# So basically for the full house one, you have to go through, and if any of the counts are odd numbers, 
# you have to assume there's 1 triple and you take out 3 (keep track of how many triples there are)
# afteerwards each number bucket will be even number
# so now if you multiply the number of triples you had in the first step by 2 (you get how many pairs you'd need to complete the triples)
# and SUBTRRACT that number from from the total of the remaining you calculated
# you'd get a result that is a multiple of 10
# basically divide that by 5, and you'd get how many remaining triples you need to make, so just go through and make sure you have enough buckets > 2 to do this

def FullHouse(nums):
	if not nums or len(nums) % 5 != 0:
		return False

	d = collections.defaultdict(int)
	for num in nums:
		d[num] += 1

	triples = 0
	for k, v in d.items():
		if v % 2 == 1:
			if v == 1:
				return False
			else:
				d[k] = v - 3
				triples += 1

	total_count = 0
	for v in d.values():
		total_count += v

	remaining_count = total_count - triples * 2
	triples_still_needed = remaining_count / 5

	for k, v in d.items():
		while v >= 6:
			if triples_still_needed == 0:
				return True
			v -= 6
			triples_still_needed -= 2

	if triples_still_needed != 0:
		return False
	return True