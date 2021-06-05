# https://leetcode.com/problems/reveal-cards-in-increasing-order/
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