"""from collections import defaultdict

def DFS(graph, k, curr_total_weight, curr_ele, C):
    
    if k == 0:
        DFS.max_weight = max(DFS.max_weight, curr_total_weight)
    else:
        
        for next_ele, next_wei in graph[curr_ele]:
            weight = abs(next_wei-C[curr_ele-1])
            DFS(graph, k-1, (curr_total_weight+weight)%1000000007,next_ele, C)
    return 
            

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        
        graph = defaultdict(list)
        for i in range(1, len(B)):
            graph[B[i]].append([i+1,C[i]])
            graph[i+1].append([B[i], C[B[i]-1]])
        
        DFS.max_weight = -1<<31
        DFS(graph, A, 0, 1, C)
        
        return DFS.max_weight
"""
from collections import defaultdict

def DFS(graph, k, curr_total_weight, curr_ele, C, A, visited):
    
    if k == A:
        DFS.max_weight = max(DFS.max_weight, curr_total_weight)
    else:
        visited[curr_ele] = True
        for next_ele, next_wei in graph[curr_ele]:
            weight = abs(next_wei-C[curr_ele-1])
            new_weight = (curr_total_weight+((weight*(A-k))%1000000007))%1000000007
            DFS.max_weight = max(DFS.max_weight, new_weight)
            if not visited[next_ele]:
                DFS(graph, k+1, (curr_total_weight+weight)%1000000007,next_ele, C,A,visited)
    return 
            

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        
        graph = defaultdict(list)
        visited = [False]*(len(B)+1)
        for i in range(1, len(B)):
            graph[B[i]].append([i+1,C[i]])
            graph[i+1].append([B[i], C[B[i]-1]])
        
        DFS.max_weight = -1<<31
        DFS(graph, 0, 0, 1, C, A,visited)
        
        return DFS.max_weight

o_object = Solution()
print(o_object.solve(3, [0, 1, 1, 2, 2, 3], [1, 6, 7, 21, 5, 18]))
            
            