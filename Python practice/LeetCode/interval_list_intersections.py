# https://leetcode.com/problems/interval-list-intersections/

def intervalIntersection(firstList, secondList):
    i = 0
    j = 0
    n = len(firstList)
    m = len(secondList)
    ans = []
    while i < n and j < m:
        # start with traversing i
        low = max(firstList[i][0], secondList[j][0])
        if low == firstList[i][0]:
            while j < m and low > secondList[j][1] :
                j += 1
           
        else:
            while i < n and low > firstList[i][1]:
                i += 1
           
        if i >= n or j >= m:
            break
        low = max(firstList[i][0], secondList[j][0])
        hi = min(firstList[i][1], secondList[j][1])
        if low <= hi:
            ans.append([low, hi])
        if hi == firstList[i][1]:
            i += 1
        else:
            j += 1
    return ans

def intervalIntersection(firstList, secondList):
    i = 0
    j = 0
    ans = []
    while i < len(firstList) and j < len(secondList):
        firstStart, firstEnd = firstList[i]
        secondStart, secondEnd = secondList[j]
        if firstStart <= secondEnd and secondStart <= firstEnd:
            temp = [max(firstStart, secondStart), min(firstEnd, secondEnd)]
            ans.append(temp)
        
        if firstEnd < secondEnd:
            i += 1
        else:
            j += 1
    return ans

print(intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]])==[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])
print(intervalIntersection( firstList = [[1,3],[5,9]], secondList = []))
print(intervalIntersection(firstList = [], secondList = [[4,8],[10,12]]))
print(intervalIntersection(firstList = [[1,7]], secondList = [[3,10]]))
print(intervalIntersection([[10,12],[18,19]],[[1,6],[8,11],[13,17],[19,20]]))