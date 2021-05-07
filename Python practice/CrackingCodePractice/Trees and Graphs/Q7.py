#graph, topological sort

def topologicalSort(projects, dependencies):
    graph = buildGraph(projects, dependencies)
    return sortGraph(projects, dependencies)

def buildGraph(projects, dependencies):
    