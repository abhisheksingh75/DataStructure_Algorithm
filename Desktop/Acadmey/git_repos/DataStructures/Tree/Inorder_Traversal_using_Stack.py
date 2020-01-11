# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def appendStack(curr, stack):
    while(curr):
        stack.append(curr)
        curr = curr.left
    return

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack = []
        ans = []
        curr = A
        appendStack(curr, stack)
        while(stack):
            ans.append(stack[-1].val)
            curr = stack.pop().right
            appendStack(curr, stack)
        return ans
        
        
            
            
            
            
    