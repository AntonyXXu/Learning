# https://leetcode.com/problems/lru-cache/


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.last = 0

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        else:
            self.d[key][1] = self.last
            self.last += 1
            return self.d[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = [value, self.last]
            self.last += 1
            return
        if len(self.d) == self.capacity:
            minV = None
            for k, v in self.d.items():
                if not minV:
                    minV = (v[1], k)
                else:
                    if minV[0] >= v[1]:
                        minV = (v[1], k)

            del self.d[minV[1]]
        self.d[key] = [value, self.last]
        self.last += 1


t = LRUCache(2)
t.put(1, 1)
t.put(2, 2)
print(t.get(1))
print(t.d)
t.put(2, 2)
print(t.d)
