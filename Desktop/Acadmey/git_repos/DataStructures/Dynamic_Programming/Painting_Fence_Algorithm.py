
def paintFence(n,k,prev_col, prev_col_count, ans, tmp):

    if n == 0:
        ans.append(tmp[:])
    else:
        for i in range(1,k+1):
            if i != prev_col:
                tmp.append(i)   
                paintFence(n-1,k,i,1,ans,tmp)
                tmp.pop()
            elif i == prev_col and prev_col_count < 2:
                tmp.append(i)
                paintFence(n-1,k,i,2,ans,tmp)
                tmp.pop()
    return
                
class Solution:
    
    def solve(self, n, k):
        ans = []
        paintFence(n,k,-1,0, ans, [])
        return ans
    def findNoWays(self,n,k):
        
        if n < 1 or k < 1:
            return 0
        
        same = 0
        diff = k 
        total = same + diff 
            
        for i in range(2, n+1):
            same = diff 
            diff = total*(k-1)
            total = same + diff 
        return total
        
        
o_bject = Solution()
print(o_bject.solve(3,4))
print(o_bject.findNoWays(3,4))
        