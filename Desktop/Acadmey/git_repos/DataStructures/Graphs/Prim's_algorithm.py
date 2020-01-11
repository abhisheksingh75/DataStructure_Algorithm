#time complexity ElogV
from collections import defaultdict
import heapq
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        visited = [False]*(A+1)
        heap = []
        graph = defaultdict(list)
        MST = 0
        #prepare graph adjanecy list
        for u, v, wei in B:
            graph[u].append([v, wei])
            graph[v].append([u, wei])
        print(graph)
        for u, v, wei, in B:
            heapq.heappush(heap, [0, u])
            break
        while(heap):
            wei, v = heapq.heappop(heap)
            if not visited[v]:
                #print("v:"+str(v)+"wei"+str(wei))
                visited[v] = True
                MST += wei
                for adj_node, weight in graph[v]:
                    if not visited[adj_node]:
                        heapq.heappush(heap, [weight,adj_node])
        return MST
                    
                
O_OBJECT = Solution()
print(O_OBJECT.solve(4, [[1, 2, 1],[2, 3, 4],[1, 4, 3],[4, 3, 2],[1, 3, 10]]))
        
        
        