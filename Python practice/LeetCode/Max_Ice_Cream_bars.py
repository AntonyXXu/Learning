# It is a sweltering summer day, and a boy wants to buy some ice cream bars.

# At the store, there are n ice cream bars. You are given an array costs of length n, 
# where costs[i] is the price of the ith ice cream bar in coins. 
# The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

# Return the maximum number of ice cream bars the boy can buy with coins coins.

# Note: The boy can buy the ice cream bars in any order.
costs = [1,6,3,1,2,5]
coins = 20

costs1 = [10,6,8,7,7,8]
coins1 = 5

costs2 = [1,3,2,4,1]
coins2 = 7

def maxIceCream(costs, coins):
    if not costs or coins == 0:
        return 0
    cost_copy = sorted(costs)   
    print(cost_copy)
    i = 0
    counter = 0
    while i < len(cost_copy) and coins > 0:
        if coins - cost_copy[i] >= 0:
            counter += 1
            coins -= cost_copy[i]
            i += 1
        else:
            break
    return counter

print(maxIceCream(costs,coins))
print(maxIceCream(costs1,coins1))
print(maxIceCream(costs2,coins2))