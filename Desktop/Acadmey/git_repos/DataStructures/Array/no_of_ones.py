def countNoDigits(i, A):
    chunk_size = 10**i 
    chunk_dis = chunk_size*10 
    digit = (A%chunk_dis)//chunk_size 
    
    roundDown = A-A%chunk_dis
    roundUp = roundDown+chunk_dis
    if digit == 1:
        right = A%chunk_size 
        return roundDown//10 + right + 1
    elif digit < 1:
        return (roundDown//10)
    else:
        return (roundUp//10)
    
def noOfDgitis(A):
    lenA = len(str(A))
    count = 0
    for i in range(lenA):
        count += countNoDigits(i, A)
    return count

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return noOfDgitis(A)
            
sol = Solution()
arr = 10
print(sol.solve(arr))