
class Solution:
    def solve(self,matrix):
        no_rows = len(matrix)
        no_cols = len(matrix[0])
        for i in range(no_rows-1, -1, -1):
            row = i 
            col = 0 
            diag_set = set()
            while(row<no_rows and col < no_cols):
                diag_set.add(matrix[row][col])
                row += 1
                col += 1
            if len(diag_set) > 1:
                return 0 
        for j in range(1, no_cols):
            row = 0
            col = j 
            diag_set = set()
            while(row<no_rows and col<no_cols):
                #print("matrix[row][col]:"+str(matrix[row][col])+"row:"+str(row)
                #      +"col:"+str(col))
                diag_set.add(matrix[row][col])
                row += 1
                col += 1
            if len(diag_set) > 1:
                return 0 
        return 1
                
                
            
        
sol = Solution()
print(sol.solve([[1, 2, 3, 4],[5, 1, 2, 3],[9, 5, 1, 2]]))