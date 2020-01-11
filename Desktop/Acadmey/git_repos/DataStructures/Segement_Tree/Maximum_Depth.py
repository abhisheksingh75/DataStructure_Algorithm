"""
Given a Tree of A nodes having A-1 edges. Each node is numbered from 1 to A where 1 is the root of the tree. You are given Q queries. In each query, you will be given two integers L and X. Find the value of such node which lies at level L mod (MaxDepth + 1) and has value greater than or equal to X. Answer to the query is the smallest possible value or -1, if all the values at the required level are smaller than X. Note:
It is guaranteed that each edge will be connecting exactly two different nodes of the tree.
Edges are numbered from 1 to A-1. Please read the input format for more clarification
"""
from collections import defaultdict, deque
import bisect

def findMaxDepth(Tree, curr_node, curr_depth,visited):
    
    visited[curr_node] = True
    if curr_depth > findMaxDepth.max_depth:
        findMaxDepth.max_depth = curr_depth
    for ele in Tree[curr_node]:
        if not visited[ele]:
            findMaxDepth(Tree, ele, curr_depth+1,visited)
    return 

def Tree_BFS(Tree, res, curr_node, curr_level, D, visited):
    
    que = deque()
    que.append([curr_node, curr_level])
    
    while(que):
        node, level = que.pop()
        visited[node] = True
        #print("node:"+str(node)+"level:"+str(level))
        #append weight of node
        #res[level].append(1)
        res[level].append(D[node-1])
        for child in Tree[node]:
            if not visited[child]:
                que.append([child, level+1])
    return 
        
def treeQuery(A, X):
    #print("A:"+str(A)+"X:"+str(X))
    start = 0
    end = len(A)-1
    while(start<=end):
        mid = (start+end)//2
        #print("start"+str(start)+"end:"+str(end)+"mid:"+str(mid))
        if A[mid] == X:
            #print("sfd")
            return X 
        elif A[mid]<X:
            start = mid+1
        else:
            end = mid-1
    #print("start:"+str(start))
    if start < len(A):
        return A[start]
    else:
        return -1

def treeQuery2(A, X):
    
    idx = bisect.bisect_right(A,X)
    print(idx)
    if idx > -1 and  idx<len(A)-1 and  A[idx] >= X:
        return A[idx]
    else:
        return -1
   
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F):
        max_depth = 0
        visited = [False]*(A+1)
        #prepare tree using dictionary
        Tree = defaultdict(list)
        for i in range(len(B)):
            Tree[B[i]].append(C[i])
            Tree[C[i]].append(B[i])
        #print(Tree)
        #find max depth of a tree
        findMaxDepth.max_depth = float("-inf")
        findMaxDepth(Tree,1,1, visited)
        max_depth = findMaxDepth.max_depth
        
        #prepare level order BFS for Tree
        res = [[] for i in range(max_depth)]
        visited = [False]*(A+1)
        Tree_BFS(Tree, res, 1, 0, D, visited)
        for i in range(len(res)):
            res[i].sort()
            
        #find ans for queries 
        ans = []
        for i in range(len(E)):
            level = E[i]%(max_depth)
            #print("level:"+str(level)+"res[level]"+str(res[level])+"F[i]"+str(F[i]))
            ans.append(treeQuery2(res[level],F[i]))
            #print(ans)
        return ans

object = Solution()
print(object.solve(5,[1,4,3,1],[5,2,4,4],[7,38,27,37,1],[1,1,2],[32,18,26]))
print(7x    &(1<<2))