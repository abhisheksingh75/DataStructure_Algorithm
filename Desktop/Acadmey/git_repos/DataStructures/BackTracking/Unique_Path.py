def allVisitedPath(A,matrix):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if (((A[i][j] == 1 or A[i][j] == 2 or A[i][j] == 0) and matrix[i][j] == True) or
                (A[i][j] == -1 and matrix[i][j] == False)):
                continue
            else:
                return False
    return True
     
def moveIsValid(A,visited,i,j):
    rows = len(A)
    cols = len(A[0])
    return  0<=i<rows and 0<=j<cols and A[i][j] != -1 and visited[i][j] == False

def backtrackingSolve(result, A, i,j, visited):
    #print(visited)
    x = [0,-1,0,1] 
    y = [-1,0,1,0]
    if A[i][j] == 2 and allVisitedPath(A, visited):
        result[0] += 1
    else:
        for k in range(4):
            print("i+x[k]:"+str(i+x[k])+"j+y[k]:"+str(j+y[k])+"moveIsValid(A, visited, i+x[k], j+y[k])"+str(moveIsValid(A, visited, i+x[k], j+y[k])))
            if moveIsValid(A, visited, i+x[k], j+y[k]):
                #print("i+x[k]:"+str(i+x[k])+"j+y[k]:"+str(j+y[k]))
                visited[i+x[k]][j+y[k]] = True
                backtrackingSolve(result, A, i+x[k], j+y[k], visited)
                visited[i+x[k]][j+y[k]] = False
        
    return    


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        result = [0]*1
        visited = [[False for j in range(len(A[0]))] for i in range(len(A))]
        start_i, start_j = 0,0
        #calc start_i and start_j
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    start_i = i
                    end_j = j
                    break
        print("start_i:"+str(start_i)+"start_j:"+str(end_j))
        visited[start_i][end_j] = True    
        backtrackingSolve(result, A, start_i,end_j, visited)
        return result[0]
        
sol  = Solution()
print(sol.solve([[2, -1],[0, 0],[-1, 1]]))