class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        if B[0]!=C[0] or C[-1]!=A[0]:
            return 0

        return 1


A = [1, 6, 9, 8, 3]
B = [4, 2, 5, 1, 3]
C = [4, 5, 2, 3, 1]
sol = Solution()
print(sol.solve(A,B,C))