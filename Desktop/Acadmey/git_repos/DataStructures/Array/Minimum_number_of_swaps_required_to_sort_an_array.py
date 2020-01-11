class Sol:
    
    def solve(self, arr):
        ans = 0
        visited = [-1]*len(arr)
        for i in range(len(arr)):
            if visited[i] == 1 or arr[i] == i-1:
                continue
            else:
                j = i 
                count = 0
                while(visited[j] != 1):
                    visited[j]  = 1
                    j = arr[j]-1
                    count += 1
                ans += (count-1)
        return ans
    
solution = Sol()
print(solution.solve([1, 20, 6, 4, 5 ]))
                
