from collections import defaultdict 
def adjacency_list(B,C):
    dic = {}
    
    for i in range(len(B)):
        if B[i] in dic:
            dic[B[i]].append(C[i])
        else:
            dic[B[i]] = [C[i]]
    return dic
        
def findCycle(vertex,visited,adjacencyList): 
    
    if vertex >= len(visited):
        return 
    
    visited[vertex] = 1
    if vertex in adjacencyList:
        for ele in adjacencyList[vertex]:
            if visited[ele] == 0:
                findCycle(ele,visited,adjacencyList)
            elif visited[ele] == 1:
                findCycle.isCycle = True
        visited[vertex] = 2
    else:
        visited[vertex] = 2
    
    return 
        

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        adjacencyList = {}
        adjacencyList = adjacency_list(B,C)
        findCycle.isCycle = False
        visited = [0]*(A+1)
        for i in range(1,A+1):
            findCycle(i,visited,adjacencyList)
            if findCycle.isCycle:
                return 0
        
        return 1
        

obj = Solution()
print(obj.solve(3,[1, 2],[2,3]))     

graph = defaultdict(list)
graph[1].append(1)
graph[2].append(2)
for key in graph:
    print(key)