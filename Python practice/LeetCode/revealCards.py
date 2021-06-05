# https://leetcode.com/problems/reveal-cards-in-increasing-order/
import collections

c = [17,13,11,2,3,5,7]

def revealIncreasing(cards):
    sortedCards = sorted(cards, reverse=True)
    res = []
    res.insert(0, sortedCards.pop(0))
    for i in range(len(sortedCards)):
        res.insert(0, res.pop())
        res.insert(0,sortedCards[i])
    return res

print(revealIncreasing(c))

def dequeIncreasing(cards):
    sortedCards = sorted(cards, reverse=True)
    deq = collections.deque()
    deq.appendleft(sortedCards[0])
    for i in range(1,len(sortedCards)):
        deq.appendleft(deq.pop())
        deq.appendleft(sortedCards[i])
    res = []
    for i in range(len(sortedCards)):
        res.append(deq.popleft())

    return res

print(dequeIncreasing(c))
