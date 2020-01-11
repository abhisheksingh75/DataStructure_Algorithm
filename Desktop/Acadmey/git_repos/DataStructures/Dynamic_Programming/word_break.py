class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        N = len(A)
        dic_words = {}
        DP = [[True for j in range(N)] for i in range(N)]
        for word in B:
            dic_words[word] = 1
        print(DP)
        for l in range(N):
            for row in range(0,N-l):
                col = l+row
                if A[row:col+1] in dic_words:
                    DP[row][col] = True
                else:
                    flag  = False
                    for k in range(row,col):
                        if DP[row][k] and DP[k+1][col]:
                            print("row:"+str(row)+"col:"+str(col)+"k:"+str(k))
                            DP[row][col] = True
                            flag = True
                            break
                    if not flag:
                        DP[row][col] = False
        print(DP)
        if  DP[0][N-1]:
            return 1
        else:
            return 0
                
                
o_object = Solution()
print(o_object.wordBreak("ilike",[ "i", "like", "sam", "sung" ]))