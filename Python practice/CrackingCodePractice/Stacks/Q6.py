#Animal Shelter
from collections import deque
#Queue

class Animal:
    def __init__(self, name, order = None):
        self.name = name
        self.order = order

class Cat(Animal):
    def __init__(self, name, order = None):
        super().__init__(name, order)

class Dog(Animal):
    def __init__(self, name, order = None):
        super().__init__(name, order)

class AnimDQ:
    def __init__(self):
        self.order = 0
        self.cat = deque()
        self.dog = deque()
    def enQ(self, animal):
        animal.order = self.order
        self.order+=1    
        if isinstance(animal, Cat):
            self.cat.append(animal)
        if isinstance(animal, Dog):
            self.dog.append(animal)
    def peekCat(self):
        if len(self.cat):
            return self.cat[0]
    def peekDog(self):
        if len(self.dog):
            return self.dog[0]
    def deQCat(self):
        if not len(self.cat):
            return    
        return self.cat.popleft()
    def deQDog(self):
        if len(self.dog):
            return self.dog.popleft()
    def peek(self):
        if not len(self.cat) and not len(self.dog):
            return None
        if self.peekCat().order > self.peekDog().order:
            return self.dog[0]
        else:
            return self.cat[0]
    def deQ(self):
        if not self.peekDog():
            return self.deQCat()
        elif not self.peekCat():
            return self.deQDog()
        elif self.peekDog().order > self.peekCat().order:
            return self.deQCat()
        else:
            return self.deQDog()


    

anim = AnimDQ()
c1 = Cat("a")
c2 = Cat("b")
d1 = Dog("A")
d2 = Dog("B")

anim.enQ(c1)
anim.enQ(d1)
anim.enQ(d2)
anim.enQ(c2)

print(anim.deQ().name)

print(anim.deQ().name)
print(anim.deQ().name)
print(anim.deQ().name)

