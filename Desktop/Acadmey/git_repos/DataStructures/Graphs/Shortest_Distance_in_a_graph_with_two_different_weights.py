from collections import defaultdict, deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer  
    def solve(self,A,B,C,D):
        V = A
        pathLen = 0
        que = deque()
        graph = defaultdict(list)
        for u,v, w in B:
            if w == 1:
                graph[u].append(v)
                graph[v].append(u)
            else:
                graph[u].append(V)
                graph[V].append(v)
                graph[v].append(V)
                graph[V].append(u)
                V += 1
        print(graph)
        visited = [False]*V 
        que.append(C)
        visited[C] = True
        que.append('$')
        while(que):
            print(que)
            u = que.popleft()
            if u == '$':
                if que:
                    que.append('$')
                    pathLen += 1
                    continue
                else:
                    return -1
            
            if u == D:
                return pathLen
            
            for v in graph[u]:
                if visited[v] == False:
                    que.append(v)
            visited[u] = True
        return -1

object = Solution()
print(object.solve(5,[[0, 2, 1],[0, 4, 2],[1, 3, 1],[1, 4, 1],[0, 1, 1],[2, 4, 1],[3, 4, 2],[1, 2, 1]],1,3))

            
                