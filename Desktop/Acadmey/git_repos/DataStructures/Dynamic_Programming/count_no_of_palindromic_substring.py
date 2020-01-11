class Solution:
    def solve(self, A):
        ans = 0
        for i in range(len(A)):
            hashset = {}
            left_ptr = i 
            right_ptr = i+1 
            while(left_ptr>=0 and right_ptr<len(A) and A[left_ptr] == A[right_ptr]):
                hashset[A[left_ptr:right_ptr+1]] = 1 
                left_ptr -= 1
                right_ptr += 1
    
            left_ptr = i-1
            right_ptr = i+1 
            while(left_ptr>=0 and right_ptr<len(A) and A[left_ptr] == A[right_ptr]):
                hashset[A[left_ptr:right_ptr+1]] = 1 
                left_ptr -= 1
                right_ptr += 1
                
            ans += len(hashset)+1
        return ans 

sol = Solution()
print(sol.solve("aaaaa"))