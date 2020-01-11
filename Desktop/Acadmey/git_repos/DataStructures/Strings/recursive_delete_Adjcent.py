def recursiveDelete(A, res, idx):
    if idx == -1:
        return 
    else:
        if (idx-1 >= 0  and  idx+1 < len(A)):
            if (A[idx] != A[idx-1] and A[idx] != A[idx+1]):
                res.append(A[idx])
        elif idx-1 >= 0:
            if (A[idx] != A[idx-1]):
                res.append(A[idx])
        elif idx+1 < len(A):
            if A[idx] != A[idx+1]:
                res.append(A[idx])
        
        recursiveDelete(A, res, idx-1)
class Solution:
    def solve(self, A):
        while(True): 
            res = []
            recursiveDelete(A, res, len(A)-1)
            res =  "".join(res[::-1])  
            for i in range(len(res)-1):
                if res[i] == res[i+1]:
                    A = res
                    break
            if i == len(res)-2:
                break
        return res
        
        
        

sol = Solution()
print(sol.solve("mississipie"))
print(sol.solve("acaaabbbacdddd"))
