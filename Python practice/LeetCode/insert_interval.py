# https://leetcode.com/problems/insert-interval/

def insert(intervals, newInterval):
    if not intervals:
        return [newInterval]
    newLo = newInterval[0]
    newHi = newInterval[1]
    ansLeft = []
    ansRight = []
    for interval in intervals:
        if interval[1] < newLo:
            ansLeft.append(interval)
        elif interval[0] > newHi:
            ansRight.append(interval)
        else:
            newLo = min(interval[0], newLo)
            newHi = max(interval[1], newHi)
    return ansLeft + [[newLo, newHi]] + ansRight

print(insert(  intervals = [[1,3],[6,9]], newInterval = [2,5] ))
print(insert(  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8] ))
print(insert(  intervals = [], newInterval = [5,7] ))
print(insert(  intervals = [[1,5]], newInterval = [2,3] ))
print(insert(  intervals = [[1,5]], newInterval = [2,7] ))
print(insert(  intervals = [[0,0],[1,1], [7,10]], newInterval = [2,7] ))
