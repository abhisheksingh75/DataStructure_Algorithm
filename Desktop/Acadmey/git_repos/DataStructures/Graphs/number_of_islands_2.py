from collections import deque
def isSafe(i,j,isVisited,A):
    
    if (0<=i<len(A)) and (0<=j<len(A[0])) and isVisited[i][j] == False:
        isVisited[i][j] = True    
        if A[i][j] == 1:
            return True
        else:
            return False
    return False    
        

def BFS(row,col,isVisited,A):
    
    
    rowNo = [-1,-1,-1,0,0,1,1,1]
    colNo = [-1,0,1,-1,1,-1,0,1]
    
    
    que = deque()
    que.append((row,col))
    
    while(que):
        i,j = que.popleft()
        print("i:"+str(i)+"j:"+str(j))
        for k in range(8):
            if isSafe(i+rowNo[k],j+colNo[k],isVisited,A):
                que.append((i+rowNo[k],j+colNo[k]))
            
    return 

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A = [[1 for j in range(100)] for i in range(100)]
        cnt = 0
        isVisited = [[False for j in range(len(A[0]))] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if isVisited[i][j] == False:
                    isVisited[i][j] = True
                    if A[i][j] == 1:
                        BFS(i,j,isVisited, A)
                        cnt += 1
        return cnt
                
o_object = Solution()
print(o_object.solve([[0, 0, 1, 0, 1, 0, 1, 1, 1],[0, 1, 0, 0, 1, 1, 1, 0, 1]]))