class Vehicle:
    color = "white"
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage, capacity)
    
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)
    
    def fare(self):
        total = super().fare()
        return total + total * 0.1


b = Bus('a', 1, 2, 3)
print(b.seating_capacity())
print(Bus.color)
print(b.color)
print(type(b))
print(isinstance(b, Vehicle))