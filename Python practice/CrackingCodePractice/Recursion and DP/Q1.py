# Count the number of ways a kid can hop up either 1, 2, 3 steps at a time

def countSteps(steps):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1
    else:
        return countSteps(steps-1) + countSteps(steps-2) + countSteps(steps-3)

print(countSteps(3))
print(countSteps(5))
        

def countStepsMemo(steps):
    memo = [-1]*(steps+1)
    return helper(steps, memo)

def helper(steps, memo):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1
    elif memo[steps] >= 0:
        return memo[steps]
    else:
        memo[steps] = helper(steps-1, memo) + helper(steps-2, memo) + helper(steps-3, memo)
        return memo[steps]

print(countStepsMemo(110))
    
    


