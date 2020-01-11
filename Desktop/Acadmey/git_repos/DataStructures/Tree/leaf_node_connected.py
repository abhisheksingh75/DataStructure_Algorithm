from collections import defaultdict
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
# Tree Class
class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(Node)
    def Insert(self,parent, child,dir):
        if self.root is None:
            root_node = Node(parent)
            child_node = Node(child)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node
            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node
            return
        parent_node = self.map_nodes[parent]
        child_node = Node(child)
        self.map_nodes[child] = child_node
        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        return
def markleafNodes(node):
    if node is None or node.data == "$":
        return 
    elif node.data < 0:
        node.data = "$"
        return 
    else:
        node.val =  -1 * node.data
        markleafNodes(node.left)
        markleafNodes(node.right)
        if node.data != "$":
            node.data =  -1 * node.data 
def preorder(node):
    if node is None:
        return 
    else:
        print("node::"+str(node.data))
        preorder(node.left)
        preorder(node.right)
        
def findTreeHeight(root):
    #code here
    markleafNodes(root)
    preorder(root)
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(str, input().strip().split()))  # parent child info in list
        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the nodes in tree.
        
        print(findTreeHeight(tree.root))

''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
