from math import floor, ceil, sqrt
def calcLnBh(l,b,n, dic, ans):
    if (l,b) not in dic:
        dic[(l,b)] = 1
    else:
        return 
    
    if n <= (l*b) <= (n+2):
        if ans:
            if abs(l-b) < abs(ans[0]-ans[1]):
                ans[0], ans[1] = l,b
        else:
            ans.append(l)
            ans.append(b)
       
    if (l+1)*b <= (n+2):
        calcLnBh(l+1,b,n, dic, ans)   
    if  (l)*(b+1) <=(n+2):
        calcLnBh(l,b+1,n, dic, ans)  
    return 
    
class Solution:
    def solve(self,n):
        dic = {}
        ans = []
        ln, bh = int(floor(sqrt(n))), 1#int(ceil(sqrt(n)))
        calcLnBh(ln, bh, n, dic,ans)
        print(dic)
        return ans
    
        
sol = Solution()
print(sol.solve(1000))