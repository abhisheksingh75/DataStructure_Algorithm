class Solution:
    def duplicateZeros(self, arr) -> None:
        
        cnt_zeros = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                cnt_zeros += 1
        i = len(arr)-1
        end_idx = len(arr)-1
        int_zeros = cnt_zeros
        curr_count = 0
        while(True):
            if arr[i] == 0:
                cnt_zeros -= 1
            if not (len(arr)-i-1 < cnt_zeros and i >=0):
                break
            i -= 1
        print(i)    
        while(cnt_zeros != 0 and end_idx >=0 and i >=0):
            if arr[i] != 0:
                arr[end_idx] = arr[i]
            else:
                arr[end_idx] = 0 
                end_idx -= 1
                if end_idx >= 0:
                    arr[end_idx] = 0 
                cnt_zeros -= 1
            i -= 1
            end_idx -= 1
                
        return arr  
            
            
sol = Solution()
print(sol.duplicateZeros([0,1,0,0]))