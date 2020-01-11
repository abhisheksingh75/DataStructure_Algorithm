import sys
def findLCS(A,B):
    len_A = len(A)
    len_B = len(B)
    if len(A) <= 0 or len(B) <= 0:
        return 0
    DP = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]
    
    for i in range(1,len_A+1):
        for j in range(1, len_B+1):
            if A[i-1] == B[j-1]:
                DP[i][j] = DP[i-1][j-1]+1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
                
    if findLngBS.max_value < DP[len_A][len_B]:
       findLngBS.max_value = DP[len_A][len_B]
        
def findLngBS(a, start, end):
    
    if start < end:
        mid = (start+end)//2
        findLngBS(a,start,mid)
        findLngBS(a,mid+1,end)
        findLCS(a[start:mid+1],a[mid+1:end+1])
    return


class Solution:
    def sol(self, a):
        findLngBS.max_value = -1*sys.maxsize
        findLngBS(a, 0, len(a))
        return findLngBS.max_value*2
        

o_bject = Solution()
print(o_bject.sol("asdfdsasdf"))