
def findArragngement(n,arr,visited, ans, tmp, start):
    
    if n == start:
        ans.append(tmp[:])
    else:
        for ele in arr[start]:
            if visited[ele]:
                continue
            else:
                visited[ele] = True
                tmp.append(ele)
                findArragngement(n, arr, visited, ans, tmp, start+1)
                tmp.pop()
                visited[ele] = False
    return 

class Solution:
    def findCapWearArrange(self,N,arr):
        visited = [False]*(100+1)
        ans = []
        findArragngement(N,arr, visited, ans,[],0)
        return ans


o_bject  = Solution()
print(o_bject.findCapWearArrange(3,[[5,100,1],[2],[5,100]]))
