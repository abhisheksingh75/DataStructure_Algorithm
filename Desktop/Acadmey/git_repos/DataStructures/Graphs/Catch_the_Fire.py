''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from collections import deque
def ispathPossible(matrix, row, col):
    if  0<=row<len(matrix) and 0<=col<len(matrix[0]) and matrix[row][col] == 0:
        return True 
    else:
        return False

def main():
 # Write code here
    row_k = [0,-1,0,1]
    col_k = [-1,0,1,0]
    row, col = list(map(int,input().strip().split()))
    matrix = []
    for i in range(row):
        row_val = list(map(int,input().strip().split()))
        matrix.append(row_val)
    que = deque()
    
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                que.append([i,j])
    if que:
        que.append([-1,-1])
    count = 0 
    
    while(que):
        row, col = que.popleft()
        if row == -1 and col == -1:
            if que:
                que.append([-1,-1])
            else:
                break 
            count += 1
        for k in range(4):
            #print("row"+str(row+row_k[k])+"col:"+str)
            if ispathPossible(matrix, row+row_k[k], col+col_k[k]):
                matrix[row+row_k[k]][col+col_k[k]] = 1
                que.append([row+row_k[k],col+col_k[k]])
        
    print(count)
              
main()

