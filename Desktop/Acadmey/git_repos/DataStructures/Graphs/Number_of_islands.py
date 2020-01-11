
def DFS(i,j,isVisited, N, M, A):
    print("i:"+str(i)+"j:"+str(j))
    if (0 <= i-1 < N) and (0<=j<M) and isVisited[i-1][j] == False:
        isVisited[i-1][j] == True
        if A[i-1][j] == 1:
            DFS(i-1,j,isVisited,N,M,A)
            
    if (0 <= i < N) and (0<=j-1<M) and isVisited[i][j-1] == False:
        isVisited[i][j-1] == True
        if A[i][j-1] == 1:
            DFS(i,j-1,isVisited,N,M,A)

    if (0 <= i+1 < N) and (0<=j<M) and isVisited[i+1][j] == False:
        isVisited[i+1][j] == True
        if A[i+1][j] == 1:
            DFS(i+1,j,isVisited,N,M,A)

    if (0 <= i < N) and (0<=j+1<M) and isVisited[i][j+1] == False:
        isVisited[i][j+1] == True
        if A[i][j+1] == 1:
            DFS(i,j+1,isVisited,N,M,A)

    if (0 <= i-1 < N) and (0<=j-1<M) and isVisited[i-1][j-1] == False:
        isVisited[i-1][j-1] == True
        if A[i-1][j-1] == 1:
            DFS(i-1,j-1,isVisited,N,M,A)

    if (0 <= i+1 < N) and (0<=j+1<M) and isVisited[i+1][j+1] == False:
        isVisited[i+1][j+1] == True
        if A[i+1][j+1] == 1:
            DFS(i+1,j+1,isVisited,N,M,A)

    if (0 <= i-1 < N) and (0<=j+1<M) and isVisited[i-1][j+1] == False:
        isVisited[i-1][j+1] == True
        if A[i-1][j+1] == 1:
            DFS(i-1,j+1,isVisited,N,M,A)

    if (0 <= i+1 < N) and (0<=j-1<M) and isVisited[i+1][j-1] == False:
        isVisited[i+1][j-1] == True
        if A[i+1][j-1] == 1:
            DFS(i+1,j-1,isVisited,N,M,A)
    
    return


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        cnt = 1
        isVisited = [[False for j in range(len(A[0]))] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if isVisited[i][j] == False:
                   isVisited[i][j] == True
                   if A[i][j] == 1:
                       DFS(i,j,isVisited, len(A), len(A[0]), A)
                       cnt += 1
        return cnt
                
o_object = Solution()
print(o_object.solve([[0, 0, 1, 0, 1, 0, 1, 1, 1],[0, 1, 0, 0, 1, 1, 1, 0, 1]]))