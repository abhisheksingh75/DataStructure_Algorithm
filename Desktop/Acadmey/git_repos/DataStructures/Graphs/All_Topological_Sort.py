from collections import defaultdict
def backtracking_topo_Sort(graph, vertices, indg, ans, tmp):
    if len(tmp) == vertices:
        ans.append(tmp[:])
        return 
    else:
        for i in range(vertices):
            if indg[i] == 0:
                tmp.append(i)
                #redduce indg of neighbour:
                for v in graph[i]:
                    indg[v] -= 1
                indg[i] = -1 
                backtracking_topo_Sort(graph, vertices, indg, ans, tmp)
                for v in graph[i]:
                    indg[v] += 1
                indg[i] = 0 
                tmp.pop()
            else:
                continue
    return 

class Solution:
    def solve(self, edges, vertices):
        indg = [0]*vertices
        graph = defaultdict(list)
        ans = []
        for u, v in edges:
            graph[u].append(v)
            indg[v] += 1
        backtracking_topo_Sort(graph, vertices, indg, ans, [])
        return ans

        
o_object = Solution()
print(o_object.solve([[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]],6))  