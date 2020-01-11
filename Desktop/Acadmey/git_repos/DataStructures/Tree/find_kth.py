
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
def insert_node(root, node):
    # print root, node
    ptraverse = root
    curparent = root
    while(ptraverse != None):
        curparent = ptraverse
        if node.data<ptraverse.data:
            ptraverse.key+=1
            ptraverse=ptraverse.left
        else:
            ptraverse=ptraverse.right
    if root is None:
        root = node
    elif node.data<curparent.data:
        curparent.left=node
    else:
        curparent.right=node
    return root
def build_bst(root, arr, n):
    for it in range(n):
        root = insert_node(root, Node(arr[it], 0))
    return root

def findkthele(root, n):
    
    if root is None:
        return 0 
    print("root.ke:"+str(root.key)+"n:"+str(n))
    if int(root.key) == int(n):
        findkthele.ele = root.data
        print("apha")
        return 
    if root.key > n:
        return findkthele(root.left, n)
    else:
        return findkthele(root.right, n)

def printTree(root):
    if root is None:
        return "$"
    else:
        return "["+str(root.data)+":"+str(root.key)+","+printTree(root.left)+","+printTree(root.right)+"]"
    
def k_smallest_element(root, n):
    # Code here
    curr_node = root
    stack = []
    count = 0
    while(curr_node):
        stack.append(curr_node)
        curr_node = curr_node.left
    while(stack)
        ele =  stack.pop()
        count += 1
        ele.key = count 
        #print("ele.key:"+str(ele.key)+"curr_node:"+str(ele.data))
        curr_node = ele.right
        while(curr_node): 
            stack.append(curr_node)
            curr_node = curr_node.left
    print(printTree(root))
    findkthele.ele = 0 
    findkthele(root, n)
    return findkthele.ele


    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root= None
        root = build_bst(root, arr, n)
        k = int(input())
        print(k_smallest_element(root, k))
# Contributed by: Harshit Sidhwa

''' This is a function problem.You only need to complete the function given below '''
'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
'''
# your task is to complete this function
# function should return kth smallest element from the BST
