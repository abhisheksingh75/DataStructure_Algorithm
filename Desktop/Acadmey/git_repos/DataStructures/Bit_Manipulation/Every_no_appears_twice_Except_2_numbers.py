'''
Created on Nov 8, 2019

@author: abhisheksingh75
'''
class Solution:
    def solve(self, A):
        set1, set2 = [], []
        A_Xor_B = 0
        
        for i in range(len(A)):
            A_Xor_B ^= A[i]
        set_bit_i = 0
        
        for i in range(64):
            if (A_Xor_B&(1<<i)):
                set_bit_i = i
                break
            
        for i in range(len(A)):
            if (A[i]&(1<<set_bit_i)):
                set1.append(A[i])
            else:
                set2.append(A[i])
                
        num1, num2 = 0, 0
        for i  in range(len(set1)):
            num1 ^= set1[i]
        for i  in range(len(set2)):
            num2 ^= set2[i]
        print("num1:"+str(num1)+"num2:"+str(num2))


sol = Solution()
print(sol.solve([5,5,1,2,2,4,3,3,7,4]))
