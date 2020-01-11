count = 0
def findKSegments(A, k, ans, tmp,start):
    global count
    count += 1
    if k == 0:
        tmp.append(A[start:])
        #ans.append(tmp[:])
        tmp.pop()
    else:
        for i in range(start, len(A)-k):
            tmp.append(A[start:i+1])
            findKSegments(A, k-1, ans, tmp, i+1)
            tmp.pop()

class Solution:
    def solve(self, A, k):
        ans = []
        findKSegments(A,k-1,ans,[], 0)
        #return ans
    
sol = Solution()
arr = [i+1 for i in range(1001)]
print(sol.solve(arr, 100))
print(count)