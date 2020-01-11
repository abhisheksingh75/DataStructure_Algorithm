class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, A, B):
        ans = [-1]*len(B)
        infornts_heights = list(zip(B,A)) 
        infornts_heights  = sorted(infornts_heights ,reverse=False, key = lambda X:X[1])
        print(infornts_heights)
        
        for infornts, height in infornts_heights:
                count = 0
                for i in range(len(ans)):
                    if ans[i] == -1:
                        count += 1
                    if count == infornts+1:
                        ans[i] = height
                        break
        return ans 
                    
        

o_object = Solution()
print(o_object.order([5,3,2,6,1,4],[0,1,2,0,3,2]))