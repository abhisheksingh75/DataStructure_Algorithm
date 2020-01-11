# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def findSwapEle(pos, prev, node):
    if node is None:
        return None
    else:
        
        findSwapEle(pos,prev, node.left)
    
        if findSwapEle.prev is not None and findSwapEle.prev.val > node.val:
            if pos[0] is None:
                pos[0] = findSwapEle.prev 
                pos[1] = node 
            else:
                pos[2] = node  
        
        findSwapEle.prev = node 
        findSwapEle(pos,prev, node.right)
        
    return 

class Solution:
    
    def recoverTree(self, A):
        
        pos = [None for i in range(3)]
        findSwapEle.prev = None
        findSwapEle(pos, None,A)
        
        if pos[1] is None:
            return sorted([pos[0].val,pos[2].val])
        else:
            return sorted([pos[0].val,pos[1].val])
        
        
tree =  TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

o_bject= Solution()
print(o_bject.recoverTree(tree))
 
        
        