import bisect
def findCount(count, N, prev):
    
    if N == 0:
        return count 
    else:
        r1,r2,r3 = 0,0,0 
        if N >= 3:
            r1 = findCount(2*count, N-3, count)
        r2 = findCount(count+1, N-1, prev)
        if prev > 0:
            r3 = findCount(count+prev, N-1, prev)
        return max(r1,r2,r3)

class Solution:
    def solve(self, N):
        if N <= 1:
            return N
        return findCount(1, N-1, 0)

sol = Solution()
print(sol.solve(7))
A = [1,2,5,5,8]
print(bisect.bisect_right(A,-3))
print(bisect.bisect_right(A,4))
print(bisect.bisect_right(A,6))
print(bisect.bisect_right(A,10))
print(bisect.bisect_right(A,5))