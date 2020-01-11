

class Solution:
    def solve(self,no_disk, start, aux, end):
        
        if no_disk == 1:
            print("move disk from "+start+" to "+end)
        else:
            self.solve(no_disk-1, start, end, aux)
            print("move disk from "+start+" to "+end)
            self.solve(no_disk-1, aux,start,end)
        



o_bject = Solution()
print(o_bject.solve(3,'A','B','C'))