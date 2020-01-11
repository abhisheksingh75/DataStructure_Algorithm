
class newNode:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right  = None 
def print_tree(node):
    if node is None:
        return "-"
    else:
        leftsub = print_tree(node.left)
        rightsub = print_tree(node.right)
        return "[{}:{},{}]".format(node.val, leftsub,rightsub)

def newBT(node, k):
    if node is None:
        return None
    if node.left is None and node.right is None:
        if k-node.val <= 0:
            return node 
        else:
            return None 
    node.left = newBT(node.left, k-node.val)
    node.right = newBT(node.right, k-node.val)
    
    if node.left is None and node.right is None:
        return None 
    else:
        return node
    
class Solution:
    def solve(self, head, k):
        return newBT(head, k)
        
root = newNode(1)  
root.left = newNode(2)  
root.right = newNode(3)  
root.left.left = newNode(4)  
root.left.right = newNode(5)  
root.right.left = newNode(6)  
root.right.right = newNode(7)  
root.left.left.left = newNode(8)  
root.left.left.right = newNode(9)  
root.left.right.left = newNode(12)  
root.right.right.left = newNode(10)  
root.right.right.left.right = newNode(11)  
root.left.left.right.left = newNode(13)  
root.left.left.right.right = newNode(14)  
root.left.left.right.right.left = newNode(15)              
 

sol = Solution()
ll = sol.solve(root, 45)

print(print_tree(ll))
