"""
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)
"""
"""
class Sol:
    
    def cuttingRod(self, price,len_of_rod):
        if len_of_rod <= 0:
            return 0
        
        max_profit = 0
        for i in range(len(price)):
            if i+1<=len_of_rod:
                max_profit = max(max_profit, price[i]+self.cuttingRod(price,len_of_rod-(i+1)))
        return max_profit
                
"""
#with DP top bottom approach
"""
class Sol:
    
    def cuttingRod(self, price,len_of_rod, DP):
        if len_of_rod <= 0:
            return 0
        if DP[len_of_rod] != -1:
            return DP[len_of_rod]
        
        max_profit = 0
        for i in range(len(price)):
            if i+1<=len_of_rod:
                max_profit = max(max_profit, price[i]+self.cuttingRod(price,len_of_rod-(i+1), DP))
        DP[len_of_rod] = max_profit
        return DP[len_of_rod]

o_bject = Sol()
DP = [-1]*9
DP[0] = 0
print(o_bject.cuttingRod([1, 5, 8, 9, 10, 17, 17, 20] ,8, DP))
"""
#With Top Bottom approach

class Sol:
    
    def cuttingRod(self, price,len_of_rod):
        if len_of_rod <= 0:
            return 0
        DP = price[:]
        DP = [0] + price
        
        for i in range(len(DP)):
            max_profit = 0
            for j in range(i):
                max_profit = max(max_profit, DP[j]+DP[i-j])
            DP[i] = max_profit
        return DP[len(DP)-1]

o_bject = Sol()
DP = [-1]*9
DP[0] = 0
print(o_bject.cuttingRod([1, 5, 8, 9, 10, 17, 17, 20] ,8))

