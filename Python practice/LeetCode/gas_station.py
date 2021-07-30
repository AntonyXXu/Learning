# https://leetcode.com/problems/gas-station/

def canCompleteCircuit(gas, cost):
    if not gas or not cost:
        return -1
    totalGas = 0
    totalCost = 0
    curr = 0
    tank = 0
    for i in range(len(gas)):
        totalGas += gas[i]
        totalCost += cost[i]
        tank += gas[i] - cost[i]
        if tank < 0:
            curr = i + 1
            tank = 0
    if totalCost > totalGas:
        return -1
    return curr