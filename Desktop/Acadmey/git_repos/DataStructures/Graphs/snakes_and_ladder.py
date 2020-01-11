from collections import defaultdict
from collections import deque
class Solution:
    def getMinDiceThrow(self, N, A):
        visited = [False]*N
        for i in range(N):
            if moves[i] == -1:
                moves[i] = i
        que = deque()
        que.append([0,0])
        visited[0] = True
        
        while(que):
            pos, no_move = que.popleft()
            if pos == N-1:
                return no_move
            else:
                for i in range(1, 7):
                    if pos + i < N and visited[A[pos + i]] == False:
                        que.append([A[pos+i],no_move+1])
        
        
        

o_bject = Solution()
moves = [-1]*30
# Ladders 
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28
  
# Snakes 
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6
print(o_bject.getMinDiceThrow(30, moves))
dic_ele_count = defaultdict(lambda:[0,0])
dic_ele_count[0] = [dic_ele_count[0][0]+1, 0]
print(dic_ele_count)
print(bin(234234))
print(bin(((234234>>4)<<4)))
print(bin(123>>4))
print(bin(123<<4))
print(bin(((234234>>4)<<4)))


