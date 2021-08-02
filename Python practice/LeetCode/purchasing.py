import heapq


class Purchase:
    def __init__(self, buy, sell):
        heapq.heapify(sell)
        for i in range(len(buy)):
            buy[i] *= -1
        heapq.heapify(buy)
        self.sell = sell
        self.buy = buy
        self.profits = 0

    def compute(self):
        while self.sell[0] < -self.buy[0]:
            seller = heapq.heappop(self.sell)
            buyer = heapq.heappop(self.buy)
            self.profits += -buyer - seller
        return self.profits

    def buying(self, num):
        heapq.heappush(self.buy, -num)
        return self.compute()

    def selling(self, num):
        heapq.heappush(self.sell, num)
        return self.compute()


p = Purchase([100, 100, 99, 99, 97, 90], [109, 110, 110, 114, 115, 119])
p.compute()
print(p.buying(120))
print(p.selling(0))
