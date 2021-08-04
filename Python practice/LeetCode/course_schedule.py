# https://leetcode.com/problems/course-schedule/
import collections


def canFinish(numCourses, preReq):
    if not preReq:
        return True

    d = collections.defaultdict(list)
    # build the graph
    for edge in preReq:
        d[edge[0]].append(edge[1])

    visited = [False] * numCourses
    recursiveStack = [False] * numCourses

    for vertex in range(numCourses):
        if not visited[vertex]:
            if dfsCycle(visited, recursiveStack, vertex, d):
                return False
    return True


def dfsCycle(visited, recursiveStack, vertex, d):
    visited[vertex] = True
    recursiveStack[vertex] = True

    for neighbor in d[vertex]:
        if not visited[neighbor]:
            if dfsCycle(visited, recursiveStack, neighbor, d):
                return True
        elif recursiveStack[neighbor]:
            return True
    recursiveStack[vertex] = False
    return False


print(canFinish(2,  [[1, 0]]))
print(canFinish(2, [[1, 0], [0, 1]]))
