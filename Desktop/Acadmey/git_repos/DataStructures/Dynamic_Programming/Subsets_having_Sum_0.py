
maxSum = 100
arrSize = 51
  
# variable to store  
# states of dp  
dp = [[ 0 for j in range(maxSum)] for i in range(arrSize)]  
visit = [[ 0 for j in range(maxSum)] for i in range(arrSize)] 
  
# To find the number of subsets  
# with sum equal to 0. 
# Since S can be negative,  
# we will maxSum to it 
# to make it positive  
def SubsetCnt(i, s, arr, n) : 
      
    # Base cases  
    if (i == n) : 
        if (s == 0) : 
            return 1;  
        else : 
            return 0;  
      
    # Returns the value  
    # if a state is already solved  
    if (visit[i][s + arrSize]) : 
        return dp[i][s + arrSize];  
  
    # If the state is not visited,  
    # then continue  
    visit[i][s + arrSize] = 1;  
  
    # Recurrence relation  
    dp[i][s + arrSize ] = (SubsetCnt(i + 1, s + arr[i], arr, n) + 
                           SubsetCnt(i + 1, s, arr, n));  
  
    # Returning the value  
    return dp[i][s + arrSize];  
  
# Driver Code 
if __name__ == "__main__" :  
  
    arr = [ 2, 2, 2, -4, -4 ];  
    n = len(arr);  
  
    print(SubsetCnt(0, 0, arr, n));  
  
# This code is contributed by AnkitRai01 