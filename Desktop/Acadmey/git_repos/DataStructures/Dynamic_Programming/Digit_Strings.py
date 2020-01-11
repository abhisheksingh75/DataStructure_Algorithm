
class Solution:
    def solve(self, S, K):
        
        DP = [0]*len(S)
        DP[0] = 1
        for i in range(len(S)):
            temp = ""
            temp += S[i]
            DP[i] += DP[i-1]
z            for j in range(i-1, -1, -1):
                temp = S[j]+temp 
                if int(temp) <=K:
                    if j-1>=0:
                        DP[i] += DP[j-1]
                    else:
                        DP[i] += 1
                else:
                    break 
        print(DP)
        return DP[len(S)-1]
        
                    
sol = Solution()
print(sol.solve("34212", 27))