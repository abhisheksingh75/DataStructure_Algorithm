import sys 

class Solution:
    def solve(self, amount, coins, DP):
        if DP[amount] != -1:
            return DP[amount]
        if amount == 0:
            DP[amount] = 1
            return DP[amount]
        else:
            no_of_ways = 0
            for i in range(len(coins)):
                if amount >= coins[i]:
                    no_of_ways += self.solve(amount-coins[i], coins, DP)
            DP[amount] = no_of_ways
            return DP[amount]

sol = Solution()
amount = 4
DP = [-1]*(amount+1)
ans = sol.solve(amount, [1,2,3,4], DP)//2
print(ans)