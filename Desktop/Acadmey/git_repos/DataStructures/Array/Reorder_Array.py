"""
Reorder an array according to given indexes
"""
from array import array
class Solution:
    
    def reOrder(self, arr, indx):
        N = 1<<32
        for i in range(len(arr)):
            arr[indx[i]] = N*(arr[i]%N) + arr[indx[i]]%N
            
        for i in range(len(arr)):
            arr[i] = arr[i]//N
        return arr

o_bject = Solution()
print(o_bject.reOrder([50, 40, 70, 60, 90],[3,  0,  4,  1,  2]))
        
        
        