# https://leetcode.com/problems/count-and-say/

def countAndSay(n):
    if n == 1:
        return "1"
    
    previous = [1]
    current = []
    for i in range(1, n):
        count = 1
        for j in range(len(previous) - 1):
            if previous[j] == previous[j+1]:
                count += 1
            else:
                current.append(count)
                current.append(previous[j])
                count = 1
        current.append(count)
        current.append(previous[-1])
        previous = current
        current = []
    return "".join([str(i) for i in previous])

print(countAndSay(4))
print(countAndSay(6) == "312211")