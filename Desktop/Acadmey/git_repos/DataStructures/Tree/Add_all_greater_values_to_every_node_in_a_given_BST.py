class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None  


def addGreaterValueBST(node):
    
    if node is None:
        return 
    else:
        addGreaterValueBST(node.right)
        node.val += addGreaterValueBST.curr_total
        addGreaterValueBST.curr_total = node.val
        addGreaterValueBST(node.left)

def inorder(node,inorder_list):
    if node is None:
        return 
    else:
        inorder(inorder.left)
        inorder_list.append(node.val)
        inorder(inorder.right)
    return

class Solution:
    def solve(self, head):
        addGreaterValueBST.curr_total = 0
        addGreaterValueBST(head)
        inorder_list = []
        inorder(head, inorder_list)
        return inorder_list


tree =  Node 

sol = Solution()
new_tree =  sol.solve(tree)
print("sddfcsd",end= " ")