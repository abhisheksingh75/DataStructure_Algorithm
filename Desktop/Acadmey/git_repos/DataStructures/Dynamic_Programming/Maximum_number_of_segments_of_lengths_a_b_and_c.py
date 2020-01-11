from sys import maxsize
def maxSegTopToBottom(N,segment_size,dic_ans):
    if N in dic_ans:
        return dic_ans[N]
    if N < 0:
        return -1*maxsize 
    if N == 0:
        return 0
    seg_len = -1*maxsize
    for val in segment_size:
        seg_len = max(seg_len, maxSegTopToBottom(N-val, segment_size,dic_ans))
    dic_ans[N] = seg_len+1
    return dic_ans[N]    

    
class Solution:
    def solve(self, N, a,b,c):
        dic_ans = {}
        return maxSegTopToBottom(N,[a,b,c],dic_ans)


sol = Solution()
print(sol.solve(17,2,1,3))