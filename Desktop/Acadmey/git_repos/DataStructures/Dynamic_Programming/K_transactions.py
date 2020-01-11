

def max_profit(A, k, N, profit, buy_flag):
    
    if N == len(A) or k == 0:
        return profit
    if buy_flag:
        return max(max_profit(A, k, N+1, profit-A[N], False),max_profit(A, k, N+1, profit, True))
    else:
        return max(max_profit(A, k-1, N+1, profit+A[N], True),max_profit(A, k, N+1, profit, False))  
    
class Solution:
    def solve(self, A, k):
        return max_profit(A, k, 0, 0, True)
  
    
print(bin(~(1<<1)))
print(bin(7&(~(1<<1))))      
o_sol = Solution()
testcases = int(input())
for i in range(testcases):
    k = int(input())
    N = int(input())
    stock_prices = list(map(int, input().strip().split()))
    print(o_sol.solve(stock_prices, k))
    
    
