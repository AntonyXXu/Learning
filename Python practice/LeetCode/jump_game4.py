# https://leetcode.com/problems/jump-game-vii/
import collections

def canReach(s, minJump, maxJump):
    if len(s) <= 1:
        return True
    dq = collections.deque([0])
    maxIndex = 0
    while dq:
        index = dq.popleft()
        for i in range(max(index + minJump, maxIndex + 1), min(index + minJump + 1, len(s))):
            if s[i] == len(s) - 1:
                return True
            if s[i] == 0:
                dq.append(i)
        maxIndex = max(maxIndex, index + maxJump)
    return False