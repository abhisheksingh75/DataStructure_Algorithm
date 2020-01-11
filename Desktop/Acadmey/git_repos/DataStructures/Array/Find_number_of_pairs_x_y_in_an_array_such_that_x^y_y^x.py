
def findUpperBound(k, arr):
    
    first, last = 0, len(arr)-1
    while(first<=last):
        mid  = (first + last)//2
        if arr[mid] > k:
            last = mid-1
        else:
            first = mid + 1
    return first 
        
    

class Solution:
    def solve(self, arr1, arr2):
        arr2.sort()
        count_of_zero_arr2 = 0
        ans = 0
        for i in range(len(arr2)):
            if arr2[i] == 0:
                count_of_zero_arr2 += 1
        for i in range(len(arr1)):
            if arr1[i] == 0:
                continue 
            elif arr1[i] == 1:
                ans += count_of_zero_arr2
            else:
                upper_bound = findUpperBound(arr1[i],arr2)
                ans += (len(arr2)-upper_bound)
            print(ans)
        return ans 

sol = Solution()
print(sol.solve([2, 1, 6],[1,5]))

print(2&(1<<1))
