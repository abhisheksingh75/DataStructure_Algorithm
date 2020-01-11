

class Sol:
    def solve(self, N):
        if N <= 1:
            return N
        dp = [0]*(N+1)
        dp[1] = 1
        for i in range(2, N+1):
            if i%2 == 0:
                dp[i] = 1+min(dp[i-1],dp[i//2])
            else:
                dp[i] = 1+dp[i-1]
        return dp[N]


sol = Sol()
print(sol.solve(8))