from collections import defaultdict, deque

def isSafe(A,N, i,j, visited):
    
    if  0<=i<N and 0<=j<N and A[i][j] != 'X' and visited[i][j] == False:
        return True
    else:
        return False
        
class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        N = len(A)
        Rx, Ry, Kx, Ky, Qx, Qy = -1,-1,-1,-1,-1,-1
        for i in range(N):
            for j in range(N):
                if A[i][j] == 'K':
                    Kx, Ky = i, j
                elif A[i][j] == 'Q':
                    Qx, Qy = i, j 
                elif A[i][j] == 'R':
                    Rx, Ry = i, j 
                
                if Kx != -1 and Qx != -1 and Rx != -1:
                    break
        visited = [[False for i in range(N)] for j in range(N)]
        for i in range(N):
            A[i] = list(A[i])
        
        #mark all direction in X
        for idx in range(N):
            
            if Rx != -1:
                #mark node as X in rock direction
                A[Rx][idx] = 'X'
                A[idx][Ry] = 'X'
            if Qx != -1:
                #mark node as X in Q move direction
                A[Qx][idx] = 'X'
                A[idx][Qy] = 'X'
                
                #left upper diagonal  direction 
                if Qx-idx-1 >= 0 and Qy-idx-1 >= 0:
                    A[Qx-idx-1][Qy-idx-1] = 'X'
                #right upper diagonal direction
                if Qx-idx-1 >= 0 and Qy+idx+1 < N:
                    A[Qx-idx-1][Qy+idx+1] = 'X'
                #left lower diagonal direction
                if Qx+idx+1 < N and Qy-idx-1 >= 0:
                    A[Qx+idx+1][Qy-idx-1] = 'X'
                #right lower diagonal direction
                if Qx+idx+1 < N and Qy+idx+1 < N:
                    A[Qx+idx+1][Qy+idx+1] = 'X'
        print(A)
        print("Qx:"+str(Qx)+"Qy"+str(Qy))
        #check if knight is placed on knockdown position
        if A[Kx][Ky] != 'X':
            count = 1
        else:
            return -1
        
        rowNo = [-1,-2,-2,-1,1,2,2,1]
        colNo = [-2,-1,1,2,2,1,-1,-2]
        que = deque()
        
        que.append([Kx,Ky])
        visited[Kx][Ky] = True
        while(que):
            x, y = que.popleft()
            for i in range(8):
                if isSafe(A,N,x+rowNo[i], y+colNo[i], visited):
                    que.append([x+rowNo[i],y+colNo[i]])
                    visited[x+rowNo[i]][y+colNo[i]] = True
                    count += 1
        return count

o_bject  = Solution()
print(o_bject.solve([ ".........", "K........", ".........", ".........", ".........", ".........", ".......Q.", ".........", "........." ]))