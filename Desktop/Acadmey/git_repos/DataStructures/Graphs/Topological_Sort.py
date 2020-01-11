from collections import defaultdict, deque
def DFS_topological_sort(i, graph,visited, ans):
    
    visited[i] = True
    stack = deque()
    stack.append(i)
    while(stack):
        u = stack[-1]
        child = False
        for v in graph[u]:
            if visited[v] == False:
               visited[v] = True
               stack.append(v)
               child = True
        if child == False:
            ans.append(u)
            stack.pop()

class Solution(): 
    def solve(self, edges, vertices):
        ans = []
        visited = [False]*vertices
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            
        for i in range(vertices):
            
            if visited[i] == False:
                DFS_topological_sort(i, graph, visited,ans)
        return ans[::-1]
        
        
o_object = Solution()
print(o_object.solve([[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]],6))  