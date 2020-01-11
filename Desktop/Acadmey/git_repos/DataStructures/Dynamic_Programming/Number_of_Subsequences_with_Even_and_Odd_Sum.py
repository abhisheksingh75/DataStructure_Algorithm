
def countOddSumSubSeq(A, N, curr_sum, DP):
    
    if str(N)+":"+str(curr_sum) in  DP:
        return DP[str(N)+":"+str(curr_sum)]
    if N == -1:
        if abs(curr_sum)%2 !=0:
            return 1
        else:
            return 0 
    else:
        DP[str(N)+":"+str(curr_sum)] = countOddSumSubSeq(A, N-1, curr_sum+A[N], DP)+countOddSumSubSeq(A, N-1, curr_sum, DP)
        return DP[str(N)+":"+str(curr_sum)]
class Solv:
    def solve(self, A):
        DP = {}
        return countOddSumSubSeq(A, len(A)-1, 0, DP)
    
A = [1, 2, 2, 3]
sol =Solv()
print(sol.solve(A))



    