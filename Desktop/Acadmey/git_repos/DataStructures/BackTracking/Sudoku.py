import copy
#code
def findBox(row,col):
    add_val = 0
    if row <3:
        add_val = 0
    elif row < 6:
        add_val = 2
    else:
        add_val = 4
    return row//3+col//3+add_val


def formatAns(ans):
    output = []
    for row in range(len(ans)):
        output.append("".join(list(map(str,ans[row]))))
    return output
        

def SudokoSolution(sudoku,poss_row_val,poss_col_val,poss_box_val, cell):
    row = cell//9
    col = cell%9
    box_no = findBox(row,col)
    if cell == 81:
        SudokoSolution.ans = copy.deepcopy(sudoku)
        return
    if sudoku[row][col] != 0:
        SudokoSolution(sudoku,poss_row_val,poss_col_val,poss_box_val, cell+1) 
    else:
        
        for i in range(len(poss_box_val[box_no])):
            if poss_row_val[row][(i+1)-1] == True and poss_col_val[(i+1)-1][col] == True and poss_box_val[box_no][i] == True:
                poss_box_val[box_no][i] = False
                poss_row_val[row][(i+1)-1] = False
                poss_col_val[(i+1)-1][col] = False 
                sudoku[row][col] = i+1
                SudokoSolution(sudoku,poss_row_val,poss_col_val,poss_box_val, cell+1)
                sudoku[row][col] = 0  
                poss_box_val[box_no][i] = True
                poss_row_val[row][(i+1)-1] = True
                poss_col_val[(i+1)-1][col] = True 
    return 
            
def findSudokuSolution(sudoku):
    poss_row_val = [[True for col in range(9)] for row in range(9)]
    poss_col_val = [[True for col in range(9)] for row in range(9)]
    poss_box_val = [[True for col in range(9)] for row in range(9)]

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                poss_row_val[i][sudoku[i][j]-1] = False
                poss_col_val[sudoku[i][j]-1][j] = False
                box_no = findBox(i,j)
                poss_box_val[box_no][sudoku[i][j]-1] = False
                
    SudokoSolution.ans = []
    SudokoSolution(sudoku,poss_row_val,poss_col_val,poss_box_val, 0)
    return SudokoSolution.ans


        
class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        sudoku = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                if A[i][j] == '.':
                    row.append(0)
                else:
                    row.append(int(A[i][j]))
            sudoku.append(row)
        new_A =  findSudokuSolution(sudoku)
        for i in range(9):
            row = list(A[i])
            for j in range(9):
                row[j] = new_A[i][j]
            A[i] = "".join(list(map(str,row)))
        return A
                
sol = Solution()
print(sol.solveSudoku([ "..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6", "...2759.." ]))
