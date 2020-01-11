from bisect import bisect_left, bisect_right
def countingSort(arr, idx):
    
    output = [0]*len(arr)
    
    count = [0]*10
    
    for i in range(len(arr)):
        ele = arr[i]//(10**idx)
        count[ele%10] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    for i in range(len(arr)-1,-1,-1):
        ele = arr[i]//(10**idx)
        pos = count[ele%10]-1
        count[ele%10] -= 1
        output[pos] = arr[i]
    arr[:] = output[:]


class Solution:
        
    def radixSort(self, arr):   
        max_ele = max(arr)
        for i in range(len(str(max_ele))):
            countingSort(arr, i)
        

sol = Solution()
arr = [ 170, 45, 75, 90, 802, 24, 2, 66] 
sol.radixSort(arr) 
print(arr)
print(bisect_left(arr, 1000))
print(bisect_right(arr, 89))
  