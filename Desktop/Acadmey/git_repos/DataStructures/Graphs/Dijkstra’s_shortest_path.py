
from collections import defaultdict
import heapq
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        ans = [0]*A
        graph = defaultdict(set)
        print(graph)
        visited = [[-1 for j in range(2)] for i in range(A)]
        heap = []
        for u,v,w in B:
            graph[u].add((v,w))
            graph[v].add((u,w))
        heapq.heappush(heap,[0,[-1,C]])
        print(graph)
        while(heap):
            w,edge = heapq.heappop(heap)
            u,v = edge[0],edge[1]
            if visited[v][1] == -1:
               visited[v][0] = u 
               visited[v][1] = w
               
               for  pair in graph[v]:
                   if visited[pair[0]][1] == -1:
                       heapq.heappush(heap, [pair[1]+w, [v,pair[0]]])
            
        for i in range(len(visited)):
            ans[i] = visited[i][1] 
                 
        return ans

o_object = Solution()
print(o_object.solve(6,[[0, 4, 9],[3, 4, 6],[1, 2, 1],[2, 5, 1],[2, 4, 5],[0, 3, 7],[0, 1, 1],[4, 5, 7],[0, 5, 1]],4))
        
        