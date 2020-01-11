class Area:
    def __init__(self, a, b):
        self.a = a
        self.b = b 
 
def calc_max_steps(A,B, areas, memo, is_visited):
    if A < 0 or B < 0:
        return -1
    elif (A,B) in memo:
        return memo[(A,B)]
    else:
        curr_val = -100
        for i in range(len(areas)):
            if is_visited[i] == False:
                is_visited = [False]*3
                is_visited[i] = True 
                curr_val =  max(curr_val, 1+calc_max_steps(A+areas[i].a,B+areas[i].b,areas,memo,is_visited))
                    
     
        memo[(A,B)] = curr_val+1
        return curr_val+1
         
class Solution:
    
    def max_steps(self,A,B,areas):
        calc_max_steps.max_path = []
        memo = {}
        is_visited = [False]*3
        return calc_max_steps(A,B,areas, memo, is_visited)
        

X = Area(3,2)
Y=  Area(-5,-10)
Z=  Area(-20,5)

o_bject = Solution()
print(o_bject.max_steps(20,8,[X,Y,Z]))
print(calc_max_steps.max_path )