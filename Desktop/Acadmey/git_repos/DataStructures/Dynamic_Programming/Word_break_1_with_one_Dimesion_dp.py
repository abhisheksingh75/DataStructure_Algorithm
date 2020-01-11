class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        N = len(A)
        list1 = list(A)
        print(list1)
        dic_words = {}
        isWordBreak = [False]*N
        for word in B:
            dic_words[word] = 1
        
        for i in range(N):
            for j in range(i+1):
                
                if j == 0  and  A[j:i+1] in dic_words:
                    isWordBreak[i] = True
                    break
                if (isWordBreak[j]):
                    if A[j+1:i+1] in dic_words:
                        isWordBreak[i] = True
                        break
        print(isWordBreak)
        if isWordBreak[N-1]:
            return 1
        else:
            return 0

o_object = Solution()
print(o_object.wordBreak("abababababaaaabaabbbabbbabbababbb", [ "abbbabaa", "baabaaaab", "babaaaaaba", "b", "b", "bbaaaab", "aaabbb", "aabbbbbab", "abbb", "abaa", "aaababaab", "aabbabaa", "bab", "bbbbaabbb" ]))