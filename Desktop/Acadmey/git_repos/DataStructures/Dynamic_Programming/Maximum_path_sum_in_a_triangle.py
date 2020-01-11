def findMaxSumPath(A,row,col, curr_sum,dic_DP):
    if 0<=row<len(A) and 0<=col<=row:
        if (row, col) in dic_DP:
            return dic_DP[(row, col)]
        else:
            dic_DP[(row, col)]=  min(findMaxSumPath(A,row+1,col,curr_sum,dic_DP),findMaxSumPath(A,row+1,col+1,curr_sum,dic_DP))+A[row][col]
            return dic_DP[(row, col)]
    else:
        return 0
class Solution:
    def solve(self, A):
        dic_DP = {}
        curr_sum = 0
        return findMaxSumPath(A,0,0, curr_sum,dic_DP)
        

sol =Solution()
A  = [[2],
      [3,7],
      [8,5,6],
      [6,1,9,3]]
print(sol.solve(A))