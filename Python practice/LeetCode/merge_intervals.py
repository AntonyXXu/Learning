# https://leetcode.com/problems/merge-intervals/

def merge(intervals):
    ans = []
    if not intervals:
        return ans
    intervals.sort(key=lambda x: x[0] )
    minV = intervals[0][0]
    maxV = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] > maxV:
            ans.append([minV, maxV])
            minV = intervals[i][0]
            maxV = intervals[i][1]
        maxV = max(maxV, intervals[i][1])
    ans.append([minV, maxV])
    return ans
        

print(merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
print(merge(intervals =  [[1,4],[4,5]]))
print(merge(intervals = [ [4,5], [1,4]]))