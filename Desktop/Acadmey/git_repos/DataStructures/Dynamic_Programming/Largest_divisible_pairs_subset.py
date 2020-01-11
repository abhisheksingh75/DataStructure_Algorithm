
class Solution:
    def largestDivisiblePair(self,A):
        N = len(A)
        A.sort()
        DP = [0]*N
        max_len = float("-inf")
        for i in range(N-1,-1,-1):
            
            for j in range(i, N):
                if A[j]%A[i] == 0:
                    max_len = max(max_len, DP[j])
                    
            DP[i] = 1 + max_len 
            
        return max(DP)
            
object = Solution()
print(object.largestDivisiblePair([18, 1, 3, 6, 13, 17]))