# Definition for a  binary tree node
from collections import defaultdict 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def verticalOrderTraversalRec(node, curr_level, ans, height):
    
    if node is None:
        return
    ans[curr_level].append([node.val, height])
    verticalOrderTraversalRec(node.left, curr_level-1, ans, height+1)
    verticalOrderTraversalRec(node.right, curr_level+1, ans,height+1)
    
    
    

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        dic_ans = defaultdict(list)
        ans = []
        verticalOrderTraversalRec(A, 0, dic_ans, 0)
        for key in sorted(dic_ans):
            curr_list = dic_ans[key]
            tmp = []
            print(curr_list)
            curr_list.sort(key = lambda x:x[1])
            ans.append([x[0] for x in curr_list])
        return ans
    
        
Tree  = TreeNode(6)

Tree.left = TreeNode(3)
Tree.left.left = TreeNode(2)
Tree.left.right = TreeNode(5)

Tree.right = TreeNode(7)
Tree.right.right = TreeNode(9)

sol = Solution()
print(sol.verticalOrderTraversal(Tree))
