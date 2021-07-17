# https://leetcode.com/problems/group-anagrams/
def groupAnagrams(strs):

    d = {}
    for i, s in enumerate(strs):
        key = tuple(sorted(s))
        if key not in d:
            d[key] = [i]
        else:
            d[key].append(i)
    
    ans = []
    for indexes in d.values():
        current = []   
        for index in indexes:
            current.append(strs[index])
        ans.append(current)
    
    return ans
print(groupAnagrams(       ["eat","tea","tan","ate","nat","bat"]  ))
print(groupAnagrams(       ["t"]  ))
print(groupAnagrams(       [""]  ))
