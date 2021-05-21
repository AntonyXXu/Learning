# A string s of lowercase English letters is given. We want to partition this string into as many parts as possible 
# so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# https://leetcode.com/problems/partition-labels/

s = "ababcbacadefegdehijhklij"

def partition_labels(string):
    res = []
    if not string or len(string) == 0:
        return res
    chars = {}
    for index, letter in enumerate(string):
        if letter not in chars:
            chars[letter] = [index, index]
        else:
            chars[letter][1] = index
    min_i = None
    max_i = None
    for start, end in chars.values():
        if min_i == None and max_i == None:
            min_i = start
            max_i = end
        elif start < max_i and end > max_i:
            max_i = end
        elif start > max_i:
            res.append(max_i - min_i + 1)
            min_i, max_i  = start, end
    res.append(max_i - min_i + 1)
    return res

print(partition_labels(s))
print(partition_labels(""))
print(partition_labels("a"))