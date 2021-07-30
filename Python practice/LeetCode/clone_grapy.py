# https://leetcode.com/problems/clone-graph/


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
import collections
def cloneGraph(node):
    if not node:
        return None
    if not node.neighbors:
        return Node(node.val)
    dq = collections.deque()
    dq.append(node)
    nodes = {node: Node(node.val)}
    while dq:
        curr = dq.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in nodes:
                nodes[neighbor] = Node(neighbor.val)
                dq.append(neighbor)
            nodes[curr].neighbors.append(nodes[neighbor])
    return nodes[node]