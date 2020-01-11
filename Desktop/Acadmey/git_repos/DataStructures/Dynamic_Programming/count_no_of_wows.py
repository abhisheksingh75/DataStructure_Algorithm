
class Solution:
    def solve(self, A, B):
        
        DP = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]
        
        for i in range(len(A)+1):
            DP[0][i] = 1 
        A =  " "+A
        B = " "+B 
        for i in range(1,len(B)):
            for j in range(1, len(A)):
                if A[j] == B[i]:
                    DP[i][j] = DP[i-1][j-1] + DP[i][j-1]
                elif A[j] != B[i] and B[i] == 'w' and A[j] == 'v' and j-1 >0 and A[j-1] == 'v':
                    DP[i][j] = DP[i-1][j-2] + DP[i][j-1]
                else:
                    DP[i][j] = DP[i][j-1]
        return DP[len(B)-1][len(A)-1]
    
sol = Solution()
print(sol.solve("vvowovov", "wow"))