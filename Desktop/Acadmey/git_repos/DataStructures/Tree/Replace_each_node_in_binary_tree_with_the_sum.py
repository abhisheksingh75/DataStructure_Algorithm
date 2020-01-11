"""
Given a binary tree containing n nodes. The problem is to replace each node in the binary tree with the sum of its inorder predecessor and inorder successor.
for this instance will consider pre order traversal
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getPreorderTraversal(node, arr):
    
    if node is None:
        return 
    else:
        arr.append(node.val)
        getPreorderTraversal(node.left, arr)
        getPreorderTraversal(node.right, arr)
    return

def replacePreorderTraversal(node, arr, i):
    if node is None:
        return 
    else:
        node.val = arr[i[0]-1] + arr[i[0]+1]
        i[0] += 1
        replacePreorderTraversal(node.left, arr, i)
        replacePreorderTraversal(node.right, arr, i)
    return 

def preorder(node):
    if node is None:
        return 
    else:
        print(node.val)
        preorder(node.left)
        preorder(node.right)
    return
    
class Sol:
    
    def solve(self, root):
        arr = []
        preorder(root)
        arr.append(0)
        getPreorderTraversal(root, arr)
        arr.append(0)
        i = [1]
        replacePreorderTraversal(root, arr, i)
        preorder(root)
        return root


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)

tree.left.left = Node(4)
tree.left.right = Node(5)
            
tree.right.left  = Node(6)
tree.right.right  = Node(7)

object = Sol()
print(object.solve(tree))