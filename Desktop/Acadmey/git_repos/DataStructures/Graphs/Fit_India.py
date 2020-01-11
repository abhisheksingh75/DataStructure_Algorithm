''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from collections import deque

def isPossiblePath(visited,garden, row, col, path, step):
    
    if 0<=row<8 and 0<=col<8 and garden[row][col] == path[step] and visited[row][col] == 0:
        return True
    else:
        return False
 
def findPath(visited, garden, row, col, path, step, flag):
    visited[row][col] = 1
    #base condition for recursion 
    if step == len(path)-1 or flag[0] == True:
        flag[0] = True
        return 

    x_pos = [-1,-1,-1,0,1,1,1,0]
    y_pos = [-1,0,1,1,1,0,-1,-1]
    for i in range(8):
        if isPossiblePath(visited,garden, row+x_pos[i], col+y_pos[i], path, step+1):
            findPath(visited,garden, row+x_pos[i], col+y_pos[i], path, step+1, flag)
    return

def main():
    #collect input from consol 
    garden = []
    path_len  = int(input())
    path = list(input())
    for i in range(8):
        row = list(input().strip())
        garden.append(row)
    #print(garden)
    starting_points = deque()
    #collect starting points
    for i  in range(8):
        for j in range(8):
            if garden[i][j] == path[0]:
                starting_points.append([i,j])
    
    total_path_count = 0
    #print(starting_points)
    #do DFS for each starting point
    while(starting_points):
        row, col = starting_points.popleft()
        visited  =[[0 for col in range(8)] for row in range(8)] 
        flag = [False]
        findPath(visited, garden, row, col, path, 0, flag)
        if flag[0]:
            total_path_count += 1
        #print(visited)
    return total_path_count
print(main()) 

