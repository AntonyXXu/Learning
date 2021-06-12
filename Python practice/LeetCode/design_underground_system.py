# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:
    def __init__(self):
        self._in = {}
        self._times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self._in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, start_t = self._in[id]
        if start+'_'+stationName not in self._times:
            self._times[start+'_'+stationName] = [1, t-start_t]
        else:
            current = self._times[start+'_'+stationName]
            current[0] += 1
            current[1] += t - start_t

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        num, totalTime = self._times[startStation+'_'+endStation]
        return totalTime/num

u = UndergroundSystem()
u.checkIn(1,'a',0)
u.checkOut(1,'b',5)