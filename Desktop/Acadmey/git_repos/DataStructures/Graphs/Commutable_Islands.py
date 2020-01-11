from collections import defaultdict
class Graph:
    
    def __init__(self):
        self.vertex = None
        self.graph = defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
  

def root(idx,parent):
    print(idx)
    while(idx != parent[idx]):
        idx = parent[idx]
    
    return idx
     
def disjointFind(A,B,parent):
    
    rootA = root(A,parent) 
    rootB = root(B,parent)
    if rootA == rootB:
        return True
    else:
        return False
    
def disjointUnion(A,B, parent):
    
    rootA = root(A,parent)
    rootB = root(B,parent)
    parent[rootA] = rootB
    
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        parent = [0]*(A+1)
        parentSize = [1]*(A+1)
        
        B.sort(key= lambda x:x[2])
        B.append([-1,-1,-1])
        sum = 0
        for i in range(1,A+1):
            parent[i] = i
        
        for i in range(len(B)-1):
            u,v,wei = B[i][0],B[i][1],B[i][2]
            if disjointFind(u,v,parent) == False:
                #print("("+str(B[i][0])+","+str(B[i][1])+","+str(B[i][2])+")")
                disjointUnion(u,v, parent)
                sum += wei
        return sum

object = Solution()
print(object.solve(4,  [[1, 2, 1],[2, 3, 4],[1, 4, 3],[4, 3, 2],[1, 3, 10]]))
                
                
                
                
                
                