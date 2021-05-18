# Design a system that manages the reservation state of n seats that are numbered from 1 to n.

# Implement the SeatManager class:

# SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
# int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
# void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
 
class SeatManager:
    def __init__(self, num):
        self.seats = [False for i in range(1,num+1)]

    def reserve(self):
        for i in range(len(self.seats)):
            if not self.seats[i]:
                self.seats[i] = True
                return i
    
    def unreserve(self, seat):
        if seat <= 0 or seat > len(self.seats):
            return False
        self.seats[seat] = False
        return True

class SeatManagerHeap:
    def __init__(self, num):
        self.seats = [i for i in range(1, num+1)]
        self.count = num

    def reserve(self):
        if not self.seats or self.count == 0:
            return -1
        ret_val = self.seats[0]
        self.count -= 1
        i = 0
        while (2*i+1 < self.count or 2*i+2 < self.count 
        or self.seats[i] < self.seats[2*i+1] or self.seats[i] < self.seats[2*i+2]):
            if self.seats[2*i+1] > self.seats[2*i+2]:
                self.seats[i], self.seats[2*i+1] = self.seats[2*i+1], self.seats[i]
                i = 2*i + 1
            else:
                self.seats[i], self.seats[2*i + 2] = self.seats[2*i + 2], self.seats[i]
                i = 2*i + 2
        return ret_val

    def unreserve(self, num):
        self.seats[self.count] = num
        i = self.count
        self.count += 1
        while (i-1)//2 < 0 or self.seats[i] < self.seats[(i-1)//2]:
            self.seats[i], self.seats[(i-1)//2] = self.seats[(i-1)//2], self.seats[i]
        return

