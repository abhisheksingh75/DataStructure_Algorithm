class Solution:
    def numTilings(self, N: int) -> int:
        rec = [1]*(N+1)
        if N <=1:
            return rec[N] 
        
        rec[2] = 2
        
        for i in range(3, N+1):
            rec[i] = rec[i-1] + rec[i-2] + (rec[i-3]*2)
        
        return rec[N]

o_bject = Solution()
print(o_bject.numTilings(1))