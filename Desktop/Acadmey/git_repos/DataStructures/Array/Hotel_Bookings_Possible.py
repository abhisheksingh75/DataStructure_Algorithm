
class Solution:
    def solve(self, arrival, departure, k):
        arrival_symbol = []
        for i in range(len(arrival)):
            arrival_symbol.append([arrival[i], 1])
        depart_symbol = []
        for i in range(len(departure)):
            depart_symbol.append([departure[i], 0])
        
        arrival_symbol.extend(depart_symbol)
        arrival_symbol.sort(key = lambda x:(x[0],x[1]))
        no_rooms = 0
        #print(arrival_symbol)
        for i in range(len(arrival_symbol)):
            if arrival_symbol[i][1] == 1:
                no_rooms += 1
            else:
                no_rooms -= 1
            if no_rooms > k:
                return 0
        return 1

sol = Solution()
print(sol.solve([1,2,3],[2,3,4],1))