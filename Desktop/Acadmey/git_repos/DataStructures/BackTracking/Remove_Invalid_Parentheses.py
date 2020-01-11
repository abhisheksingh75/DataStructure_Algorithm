from collections import deque

def isValidParenthese(string):
    #print("isValidParenthese(  "+str(string)+"  )")
    stack = 0
    for char in string:
        if char.isalpha():
            continue
        elif char == "(":
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                return False
    if stack != 0:
        return False
    else:
        return True
    
    

def validParenthese(A, ans, invalid_count):
    
    if invalid_count == 0:
        if isValidParenthese(A):
            ans.add(A)
    else:
        for i in range(len(A)):
            if not A[i].isalpha():
                validParenthese(A[:i]+A[i+1:], ans, invalid_count-1) 
    return
                   
class Solution:
    # @param A : string
    # @return a list of strings
    def solve(self, A):
        count,invalid_count = 0,0
        print(len(A))
        #count number of invalid character
        for i in range(len(A)):
            if A[i].isalpha():
                continue
            elif A[i] == "(":
                count += 1
            else:
                count -= 1
            if count < 0:
               invalid_count += 1
               count = 0
        invalid_count += count
        ans = set()
        print("invalid_count:"+str(invalid_count))
        validParenthese(A, ans, invalid_count)
        ans = list(ans)
        return ans
o_object = Solution()
print(o_object.solve(")(()((((()(("))