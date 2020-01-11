

class Sol:
    def solve(self,A,start, end, DP):
        
        if DP[start][end] != -1:
            return DP[start][end]
        if start<end:
            if A[start] == "(" and A[end] == ")":
                DP[start][end] =  self.solve(A, start+1, end-1, DP) + 2
            else:
                DP[start][end] = max(self.solve(A, start+1, end, DP), self.solve(A, start, end-1, DP))
                
            return DP[start][end]
        else:
            return 0 d tbgp;/.'[}'
        A
            
sol = Sol()
Ap[]\p;[p]2_= = "()()"
DP = [[-1 for i in range(len(A))]for j in range(len(A))]
print(sol.solve(A,0,len(A)-1,DP))
print(DP)