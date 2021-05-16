# https://leetcode.com/problems/find-center-of-star-graph/

e1 = [[1,2],[5,1],[1,3],[1,4]]
e2 = [[1,2],[2,3],[4,2]]
def findCenter(edges):
    x = edges[0][0]
    y = edges[0][1]
    if edges[1][0] == x or edges[1][0] == y:
        return edges[1][0]
    return edges[1][1]

print(findCenter(e1))
print(findCenter(e2))