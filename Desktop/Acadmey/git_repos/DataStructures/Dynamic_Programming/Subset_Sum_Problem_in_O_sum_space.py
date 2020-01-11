""" using recursion fing subset is possible or not 

def isSubSetSum(A,n, s):
    
    if n == -1:
        if s == 0:
            return True
        else:
            return False
    else:
        return isSubSetSum(A,n-1,s-A[n]) or isSubSetSum(A,n-1,s)


class Sol:
    def solve(self, A, sum):
        return isSubSetSum(A, len(A)-1, sum)
        
sol = Sol()
print(sol.solve([3, 34, 4, 12, 5, 2], 11))
"""

"""using recursion find subset
def isSubSetSum(A,n, s, tmp):
    #if s < 0:
    #    return False
    if n == -1:
        if s == 0:
            isSubSetSum.string = tmp
            return True
        else:
            return False
    else:
        return isSubSetSum(A,n-1,s-A[n], tmp+","+str(A[n])) or isSubSetSum(A,n-1,s, tmp)


class Sol:
    def solve(self, A, sum):
        isSubSetSum.string = ""
        isSubset =  isSubSetSum(A, len(A)-1, sum, "")
        print(isSubSetSum.string)
        return isSubset
sol = Sol()
print(sol.solve([3, 34, 4, 12, 5, 2,31,32,33,34,35,36,37,38,39,40,3,5,454,4,123,45,3,1,11,23,23,34,454,54], 100))"""
""" using recursion find subset is possible or not """

def isSubSetSum(A,n, s,dp):
    
    if s < 0:
        return False
    if n == -1:
        if s == 0:
            return True
        else:
            return False
    
    if  dp[n][s]  != -1:
        return dp[n][s]
    else:
        dp[n][s] =  isSubSetSum(A,n-1,s-A[n], dp) or isSubSetSum(A,n-1,s, dp)
        return dp[n][s]
    
    

class Sol:
    def solve(self, A, sum):
        dp = [[-1 for j in range(sum+1)] for i in range(len(A)+1)]
        is_subset =  isSubSetSum(A, len(A)-1, sum, dp)
        return is_subset

testcases = input()
testcases_list_inputs = []
for i in range(int(testcases)):
    no_ele = input()
    testcases_list_inputs.append(list(map(int,input().split())))
#print(testcases_list_inputs)
sol = Sol()
for list_inp in testcases_list_inputs:
    sum = 0
    for i in range(len(list_inp)):
        sum += list_inp[i]
    if sum%2 == 0:
        isSubset = sol.solve(list_inp, sum//2)
    else:
        print("NO")
        continue
    
    if isSubset:
        print("YES")
    else:
        print("NO")
