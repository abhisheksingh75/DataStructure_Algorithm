#code
from collections import defaultdict

def builtGraph(edges, graph):
    for i in range(0, len(edges), 2):
        graph[edges[i]].append(edges[i+1])
        graph[edges[i+1]].append(edges[i])

def isPathPossible(graph, path, no_nodes, key, visited):
    visited[key] = 1
    path.append(key)
    if isPathPossible.flag or len(path) == no_nodes:
        print(path)
        isPathPossible.flag = True
        return 
    else:
        for node in graph[key]:
            if node not in visited:
                isPathPossible(graph, path, no_nodes, node, visited)
    path.pop()
    del visited[key] 
            
def isHamiltonianPathPossible(no_nodes,no_edges,edges):
    graph = defaultdict(list)
    builtGraph(edges, graph)
    isPathPossible.flag = False
    for key in graph:
        visited = {}
        path = []
        isPathPossible(graph, path, no_nodes, key, visited)
        if isPathPossible.flag:
            return 1
    return 0
    

testcases = input()
for i in range(int(testcases)):
    no_nodes, no_edges = list(map(int, input().strip().split()))
    edges = list(map(int, input().strip().split()))
    print(isHamiltonianPathPossible(no_nodes,no_edges,edges))
    
    