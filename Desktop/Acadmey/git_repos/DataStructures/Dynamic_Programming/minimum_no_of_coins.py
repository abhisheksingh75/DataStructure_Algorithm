import sys 

class Solution:
    def solve(self, amount, coins, DP):
        if DP[amount] != -1:
            return DP[amount]
        if amount == 0:
            DP[amount] = 0
            return DP[amount]
        else:
            min_coins = sys.maxsize
            for i in range(len(coins)):
                if amount >= coins[i]:
                    min_coins = min(min_coins, 1+self.solve(amount-coins[i], coins, DP))
            DP[amount] = min_coins
            return DP[amount]

sol = Solution()
amount = 100
DP = [-1]*(amount+1)
print(sol.solve(amount, [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17], DP))