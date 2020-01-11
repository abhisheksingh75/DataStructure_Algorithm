

class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        
        A = list(A)
        N = len(A)
        
        DP = [[True for col in range(N)] for row in range(N)]
        for k in range(1, N):
            for row in range(0,N-k):
                col = row + k 
                #print("row:"+str(row)+"col:"+str(col))
                if A[row] == A[col]:
                    DP[row][col] = DP[row+1][col-1]
                    #print("DP[row][col]:"+str(DP[row][col])+"DP[row-1][col-1]"+str(DP[row-1][col-1]))
                else:
                    DP[row][col] = False
               
        cuts = [1<<31]*N
        for col in range(N):
            if DP[0][col] == True:
                cuts[col] = 0
            else:
                for row in range(col):
                    if DP[row+1][col] == True:
                        cuts[col] = min(cuts[col], cuts[row]+1)
              
        return cuts[N-1]
    

o_object = Solution()
print(o_object.minCut("BANANA"))
                    
                    
            
