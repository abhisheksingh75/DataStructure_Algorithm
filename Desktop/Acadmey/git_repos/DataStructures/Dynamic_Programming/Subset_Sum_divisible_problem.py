# Python3 program to check if there is  
# a subset with sum divisible by m. 
  
# Returns true if there is a subset 
# of arr[] with sum divisible by m 
def modularSum(arr, n, m): 
  
    if (n > m): 
        return True
  
    # This array will keep track of all 
    # the possible sum (after modulo m) 
    # which can be made using subsets of arr[] 
    # initialising boolean array with all false 
    DP = [False for i in range(m)] 
  
    # we'll loop through all the elements of arr[] 
    for i in range(n): 
      
        # anytime we encounter a sum divisible 
        # by m, we are done 
        if (DP[0]): 
            return True
  
        # To store all the new encountered sum (after 
        # modulo). It is used to make sure that arr[i] 
        # is added only to those entries for which DP[j]  
        # was true before current iteration.  
        temp = [False for i in range(m)] 
  
        # For each element of arr[], we loop through 
        # all elements of DP table from 1 to m and 
        # we add current element i. e., arr[i] to 
        # all those elements which are true in DP 
        # table 
        for j in range(m): 
          
            # if an element is true in DP table 
            if (DP[j] == True): 
              
                if (DP[(j + arr[i]) % m] == False): 
  
                    # We update it in temp and update 
                    # to DP once loop of j is over 
                    temp[(j + arr[i]) % m] = True
              
        # Updating all the elements of temp 
        # to DP table since iteration over 
        # j is over 
        for j in range(m): 
            if (temp[j]): 
                DP[j] = True
  
        # Also since arr[i] is a single element 
        # subset, arr[i]%m is one of the possible 
        # sum 
        DP[arr[i] % m] = True
      
    return DP[0] 
  
# Driver code 
arr = [3, 1, 7, 5] 
n = len(arr) 
m = 6
print("YES") if(modularSum(arr, n, m)) else print("NO") 
  
# This code is contributed by Anant Agarwal. 