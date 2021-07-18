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


def findOrder(numCourses, prerequisites):
    graph = collections.defaultdict(set)
    in_degrees = collections.defaultdict(int)
    for preReq in prerequisites:
        graph[preReq[0]].add(preReq[1])
        in_degrees[preReq[1]] += 1
    dq = collections.deque()
    for course in range(numCourses):
        if not in_degrees[course]:
            dq.append(course)

    visited = set()

    while dq:
        course = dq.popleft()
        visited.add(course)
        for neighbor in graph[course]:
            in_degrees[neighbor] -= 1
            if not in_degrees[neighbor]:
                dq.append(neighbor)
    return len(visited) == numCourses

print(findOrder(numCourses = 2, prerequisites = [[1,0]]))
print(findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
print(findOrder(numCourses = 1, prerequisites = []))
print(findOrder( numCourses = 2, prerequisites = [[1,0],[0,1]]))
print(findOrder(2,[[0,1]]))