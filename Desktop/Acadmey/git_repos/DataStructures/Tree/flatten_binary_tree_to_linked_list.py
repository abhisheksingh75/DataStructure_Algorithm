import collections
class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right  = None 

def conertBtToLL(node):
    if node:
        #assign curr not to prev node left pointer
        if conertBtToLL.prev:
            conertBtToLL.prev.left = node 
        conertBtToLL.prev = node
        conertBtToLL(node.left)
        conertBtToLL(node.right)
    return 

class Solution:
    def flatten(self, head):
        conertBtToLL.prev = None
        reversed_list =  conertBtToLL(head)
        return head 
        
        
Tree = Node(1)

Tree.left = Node(2)
Tree.right = Node(5)

Tree.left.left = Node(3)
Tree.left.right = Node(4)

Tree.right = Node(5)
Tree.right.right = Node(6)

sol = Solution()
ll = sol.flatten(Tree)
ll_list = []
while(ll):
    ll_list.append(ll.val)
    \
    ll = ll.left 
print("->".join(map(str, ll_list)))

list = [[1,2],[3,4],[6,7]]
list = list[:1]+[[1,10]]+list[1:]
print(list)
