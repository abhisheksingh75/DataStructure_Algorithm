
def findMaxProfit(A,options, profit, curr_idx):
    if curr_idx == len(A):
        #print(profit)
        return profit
    else:
        
        max_curr_profit = float("-inf")
        for i in range(3):
            #print("i:"+str(i)+"options:"+str(options)+"profit:"+str(profit)+"curr_idx:"+str(curr_idx)+"A[curr_idx]:"+str(A[curr_idx]))
            if i == 0 and options[i] == True:
                max_curr_profit = max(max_curr_profit, findMaxProfit(A,[False, True, True],profit-A[curr_idx], curr_idx+1))
            elif i == 1 and options[i] == True:
                max_curr_profit = max(max_curr_profit, findMaxProfit(A,options, profit, curr_idx+1))
            elif i == 2 and options[i] == True: 
                max_curr_profit = max(max_curr_profit, findMaxProfit(A,[True, True, False], profit+A[curr_idx], curr_idx+1))
        
        #print(max_curr_profit)
        return max_curr_profit   

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        options = [True, True, False] #[Buy, don't buy , sell]
        return findMaxProfit(A,options, 0,0)
        



O_bject = Solution()
print(O_bject.maxProfit([7,6,4,3,1]))