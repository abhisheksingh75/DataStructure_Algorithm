"""You are given N pairs of numbers. In every pair, the first number is always smaller than the second number. A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. Your task is to complete the function maxChainLen which returns an integer denoting the longest chain which can be formed from a given set of pairs. """
class Solution:
    def solve(self, pairs):
        DP = [1]*len(pairs)
        pairs.sort(key = lambda x:x[0])
        for i in range(len(pairs)):
            
            for j in range(i):
                
                if pairs[j][1] < pairs[i][0]:
                    DP[i] = max(DP[j]+1, DP[i])
        print(DP)
        return DP[len(pairs)-1]


sol = Solution()
print(sol.solve([[5, 24],[39, 60],[15, 28],[27, 40],[50, 90]]))
      