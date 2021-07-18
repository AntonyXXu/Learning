# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/?fbclid=IwAR2YCDQzjQF8Xyjq7lQb2bMfrNFbrx1ci7UJOyllgBIlDIZMTXNK-GKIckw

import collections

class Graph():
    def __init__(self, vertices):
        self.graph = collections.defaultdict(list)
        self.v = vertices

    def insert(self, edge):
        self.graph[edge[0]].append(edge[1])
    
    def cyclic(self):
        visited = [False] * (self.v + 1)
        recursive = [False] * (self.v + 1)
        for vertex in range(self.v):
            if not visited[vertex]:
                if self.cyclicHelper(vertex, visited, recursive):
                    return True
        return False

    def cyclicHelper(self, vertex, visited, recursive):
        visited[vertex] = True
        recursive[vertex] = True

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                if self.cyclicHelper(neighbor, visited, recursive):
                    return True
            elif recursive[neighbor]:
                    return True
        return False
    
g = Graph(4)
g.insert([0,1])
g.insert([0,2])
g.insert([1,2])
g.insert([2,0])
g.insert([2,3])
g.insert([3,3])

print(g.cyclic())