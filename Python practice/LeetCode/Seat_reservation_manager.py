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


