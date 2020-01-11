"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
"""
class Sol:
    
    def solve(self, set, sum):
        set.sort()
        DP = [[False for j in range(sum+1)] for i in range(2)]
        DP[0][0], DP[1][0] = True, True
        for i in range(len(set)):
            for j in range(1, sum+1):
                if j < set[i]:
                    DP[1][j] = DP[0][j]
                    continue
                else:
                    DP[1][j] = DP[0][j-set[i]]
            print(DP)
            for j in range(1, sum+1):
                DP[0][j] = DP[1][j]
        return DP[1][sum]
    
o_object = Sol()
print(o_object.solve([3, 34, 4, 12, 5, 2], 9))
        
        