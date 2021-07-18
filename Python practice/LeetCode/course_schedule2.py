# https://leetcode.com/problems/course-schedule-ii/
import collections

def findOrder(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    for preReq in prerequisites:
        graph[preReq[0]].append(preReq[1])
    
    visited = [False] * numCourses
    recursiveStack = [False] * numCourses
    ans = []

    for course in range(numCourses):
        if not visited[course]:
            if not dfs( course, visited, recursiveStack, ans, graph):
                return []
    return ans

def dfs( course, visited, recursiveStack, ans, graph):
    visited[course] = True
    recursiveStack[course] = True

    for edge in graph[course]:
        if not visited[edge]:
            if not dfs(edge, visited, recursiveStack, ans, graph):
                return False
        elif recursiveStack[edge]:
            return False
    ans.append(course)
    recursiveStack[course] = False
    return True

print(findOrder(numCourses = 2, prerequisites = [[1,0]]))
print(findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
print(findOrder(numCourses = 1, prerequisites = []))
print(findOrder(2,[[0,1]]))