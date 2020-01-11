"""merge two tress"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left  =None
        self.right = None

def preorder(node):
    if node is None:
        return 
    else:
        print(node.val)
        preorder(node.left)
        preorder(node.right)
    return

class Sol:
    def solve(self, node1, node2):
        if node1 is None and node2 is None:
            return None
        elif node1 is None and node2 is not None:
            return node2
        elif node2 is None and node1 is not None:
            return node1
        else:
            node2.val = node2.val+ node1.val
            node2.left = self.solve(node1.left, node2.left)
            node2.right = self.solve(node1.right, node2.right)
            return node2
            
        
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
            
tree.right.left  = Node(6)
tree.right.right  = Node(7)

tree2 = Node(11)
tree2.left = Node(12)
tree2.left.left = Node(13)

tree2.left.left.left  = Node(14)
tree2.left.left.right = Node(15)

object = Sol()
preorder(object.solve(tree, tree2))

