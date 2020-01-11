from pptree import *
class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

def printTree(node):
    if node is None:
        return "-"
    else:
        leftsub = printTree(node.left)
        rightsub = printTree(node.right)
        str =  "[{}:{},{}]".format(node.val, leftsub, rightsub)
        return str

class BST:
    def __init__(self):
        self.head = None 
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(str(node.val)+" ")
            self.inorder(node.right)
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
        else:
            self.bstInsert(self.head, val)
            
    def bstInsert(self, node, val):
        if node is None:
            return Node(val)
        if node.val >= val:
            node.left = self.bstInsert(node.left, val)     
        else:
            node.right = self.bstInsert(node.right, val)
        return node
    
    def search(self, val):
        return self.bstSearch(self.head,val)
    def bstSearch(self, node, val):
        if node is None:
            return None
        elif node.val == val:
            return Node
        else:
            left = self.bstSearch(node.left,val)
            if left == None:
                return self.bstSearch(node.right,val)
            else:
                return left
    def delete(self, val):
        self.bstDelete(self.head, val)
    def bstDelete(self, node, val):
        if node is None:
            return 
        elif node.val>val:
            node.left = self.bstDelete(node.left, val)
        elif node.val<val:
            node.right = self.bstDelete(node.right, val)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                node.val = node.right.val 
                node.right = None 
                return node 
            elif node.right is None:
                node.val = node.left.val 
                node.left = None 
                return node 
            else:
                succ_node = self.minvalueNode(node.right)
                node.val = succ_node.val 
                node.right = self.bstDelete(node.right, succ_node.val)
        return node
            
    def minvalueNode(self, curr):
        while(curr.left):
            curr = curr.left 
        return curr
        
    
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
print(printTree(bst.head))

bst.delete(50)
print(printTree(bst.head))
        


        