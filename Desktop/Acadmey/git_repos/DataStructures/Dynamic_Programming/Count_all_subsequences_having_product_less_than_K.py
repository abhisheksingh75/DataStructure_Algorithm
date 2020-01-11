"""
class Solution:
    def solve(self, A,k,n,curr_product, DP):
        if curr_product >= k:
            return 0 
        elif n == -1:
            if k > curr_product:
                return 1
            else:
                return 0 
        elif DP[n][k] != -1:
            return DP[n][curr_product]
        else:
            DP[n][curr_product] = self.solve(A, k, n-1,curr_product*A[n], DP) + self.solve(A,k, n-1, curr_product, DP)
            return DP[n][curr_product]

sol = Solution()
A = [4, 8, 7, 2]
k = 50
DP = [[-1 for j in range(k+1)]for i in range(len(A)+1)]
print(sol.solve(A,50,len(A)-1, 1, DP))
print(DP)"""
""" bottom top approach"""
class Solution1:
    def solve(self, A, k):
        DP = [[0 for j in range(k+1)]for i in range(len(A)+1)]
        
        for  j in range(1, k+1):
            DP[0][j] = 1
        
        for i in range(1,len(A)+1):
            for j in range(1, k+1):
                DP[i][j] = DP[i-1][j]
                if j//A[i-1] >=0:
                    print("j:"+str(j)+"A[i-1]"+str(A[i-1])+"i:"+str(i))
                    DP[i][j] += DP[i-1][j//A[i-1]]
        print(DP)
        return DP[len(A)][k]
    
sol1 = Solution1()
A = [4, 8, 7, 2]
k = 50
DP = [[-1 for j in range(k+1)]for i in range(len(A)+1)]
print(sol1.solve(A,50))
