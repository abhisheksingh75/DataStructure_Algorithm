import sys
"""Given a 2D array, find the maximum sum subarray in it. For example, in the following 2D array, the maximum sum subarray is highlighted with blue rectangle and sum of this subarray is 29."""

def findCurrSum(arr):
    
    curr_sum, global_sum, curr_i,curr_j,global_i,global_j = arr[0], arr[0], 0,0,0,0
    for i in range(1,len(arr)):
        
        if curr_sum+arr[i] < arr[i]:
            curr_i = i
            curr_j = i
            curr_sum = arr[i]
        else:
            curr_j = i 
            curr_sum = arr[i]+curr_sum
            
        if global_sum < curr_sum:
            global_sum = curr_sum
            global_i = curr_i 
            global_j = curr_j 
    
    #print("global_sum:"+str(global_sum)+"gobal_i:"+str(global_i)+"global_j:"+str(global_j))
    return [global_i,global_j,global_sum]
            

class Sol:
    def solve(self, A):
        row_wise_sum = [[0 for j in range(len(A[0]))] for i in range(len(A))]
        
        global_max_sum, global_top, global_bottom, global_left, global_right = -1*sys.maxsize,-1,-1,-1,-1
        for i in range(len(A)):
            for j in range(len(A[0])):
                
                if j ==  0:
                    row_wise_sum[i][j] = A[i][j]
                else:
                    row_wise_sum[i][j] = A[i][j] + row_wise_sum[i][j-1]
                    
        for i in range(len(A[0])):
            for j in range(i,len(A[0])):
                tmp = []
                for k in range(len(A)):
                    tmp.append(row_wise_sum[k][j]-row_wise_sum[k][i]+A[k][i])
                curr_top, curr_bottom, curr_sum = findCurrSum(tmp)
                #print(tmp)
                if curr_sum >= global_max_sum:
                    global_max_sum = curr_sum
                    global_top, global_bottom, global_left, global_right = curr_top,curr_bottom,i,j
                    
                    
        return "top left corner:("+str(global_left)+","+str(global_top)+")"+"\n"+"bottom right corner:("+str(global_right)+","+str(global_bottom)+")"
    
sol = Sol()
print(sol.solve([[1, 2, -1, -4, -20],[-8, -3, 4, 2, 1],[3, 8, 10, 1, 3],[-4, -1, 1, 7, -6]]))