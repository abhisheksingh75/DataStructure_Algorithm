from collections import defaultdict, deque

def findtoplogicalOrder(graph, in_deg, visited):
    #visited = [False]*
    ans = []
    que = deque()
    for i in range(len(in_deg)):
        if in_deg[i] == 0:
            que.append(i)
            
    while(que):
        ele = que.popleft()
        ans.append(ele)
        
        if ele in graph and visited[ele] == False:
            for dest in graph[ele]:
                in_deg[dest] -= 1
                if in_deg[dest] == 0:
                    que.append(dest)
        visited[ele] = True
        
    return ans 
    

class Solution:
    def solve(self, nodes, no_edges, edges):
        
        graph = defaultdict(list)
        in_deg = [0]*nodes
        visited = [False]*nodes
        for i in range(0, len(edges), 2):
            graph[edges[i]].append(edges[i+1])
        
        for vertex in graph:
            for dest in graph[vertex]:
                in_deg[dest] += 1
    
        return findtoplogicalOrder(graph, in_deg, visited)



        
    
      
res = 0
for count in range(10):
    res = res ^ count 
    print(res)      

sol = Solution()
testcases = input()
for i in range(int(testcases)):
    no_edges, nodes = map(int, input().split(' '))
    edges  = list(map(int, input().split(' ')))
    print(sol.solve(nodes, no_edges,edges))
