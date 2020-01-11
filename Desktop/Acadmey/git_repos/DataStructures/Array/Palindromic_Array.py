
class solution:
    def solve(self, A):
        ans = 0
        i, j = 0, len(A)-1
        while(i<=j):
            
            if A[i] == A[j]:
                i += 1
                j -= 1
            elif A[i] > A[j]:
                A[i+1] = A[i] + A[i+1]
                i += 1
                ans += 1
            else:
                A[j-1] = A[j] + A[j-1]
                ans += 1
                j -= 1
        return ans
    
sol = solution()
print(sol.solve([2,0,1]))
                