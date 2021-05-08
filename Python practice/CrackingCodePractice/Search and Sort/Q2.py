#Sort array of strings such that all anagrams are with each other

# Sort each string in the array, then sort the array

arr = []

arr.append("tset")
arr.append("agggsd")
arr.append("ttse")
arr.append("agdsgg")
arr.append("test")
arr.append("aaaa")
arr.append("tgg")
arr.append("ggt")
arr.append("gwqgwq")
arr.append("gwqgw")

def sortString(arr):
    copy = arr.copy()
    for i in range(len(copy)):
        string = sorted(copy[i])
        string = "".join(string)
        copy[i] = string
    copy.sort()
    return copy

print(sortString(arr))


def sortString2(arr):
