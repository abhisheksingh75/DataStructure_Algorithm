"""
Given is a square matrix of alphabets which contains English letters in an arbitrary manner. While searching a word in it, you can go left to right horizontally, vertically downwards or diagonally towards left (both upwards and downwards).
You have to find the number of matches of a given word in the matrix.

For example, In the given square matrix {A#A#K,A#S#K,A#K#K},

The word "ASK" is matched four times in the input matrix. So the output will be 4.


Input Format
First line contains N, size of array of string.
Next N line contains strings containing N uppercase alphabets separated by #
Second line contains String (Word to be searched)


Constraints
1 <= Size of string <= 10000

Output Format
Print number of occurrences of the word in the matrix {an integer}


Sample TestCase 1
Input
2
A#S
S#T
AS
Output
2
Explanation
The keyword AS is matched two times in the given matrix. The first row and first column makes the keyword AS.
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from collections import deque

def isPossiblePath(visited,garden, row, col, path, step):
    
    if 0<=row<len(garden) and 0<=col<len(garden[0]) and garden[row][col] == path[step] and visited[row][col] == 0:
        return True
    else:
        return False
 
def findPath(visited, garden, row, col, path, step, flag, count):
    visited[row][col] = 1
    #base condition for recursion 
    if step == len(path)-1 or flag[0] == True:
        count[0] += 1
        return 

    #x_pos = [-1,-1,-1,0,1,1,1,0]
    #y_pos = [-1,0,1,1,1,0,-1,-1]
    x_pos = [-1,1,1,0,0]
    y_pos = [-1,-1,0,1,-1]
    for i in range(5):
        if isPossiblePath(visited,garden, row+x_pos[i], col+y_pos[i], path, step+1):
            findPath(visited,garden, row+x_pos[i], col+y_pos[i], path, step+1, flag, count)
    return

def main():
    #collect input from consol 
    garden = []
    path_len  = int(input())
    for i in range(path_len):
        row = list(input().strip().split('#'))
        garden.append(row)
    path = list(input())
    #print(garden)
    starting_points = deque()
    #collect starting points
    for i  in range(len(garden)):
        for j in range(len(garden[0])):
            if garden[i][j] == path[0]:
                starting_points.append([i,j])
    
    total_path_count = 0
    #print(starting_points)
    #do DFS for each starting point
    while(starting_points):
        row, col = starting_points.popleft()
        visited  =[[0 for col in range(len(garden[0]))] for row in range(len(garden))] 
        flag = [False]
        count = [0]
        findPath(visited, garden, row, col, path, 0, flag, count)
        total_path_count += count[0]
        #print(visited)
    return total_path_count
print(main(), end = '') 

