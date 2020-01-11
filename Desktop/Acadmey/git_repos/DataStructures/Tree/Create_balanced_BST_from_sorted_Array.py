class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 


def builtBST(arr, start, end):
    
    if start == end:
        return Tree(arr[start])
    elif start > end:
        return None 
    else:
        mid  = (start+end)//2 
        node = Tree(arr[mid])
        node.left =  builtBST(arr, start, mid-1)
        node.right = builtBST(arr, mid+1, end)
        return node

def preOrderTranversal(node):
    if node is None:
        return 
    else:
        preOrderTranversal(node.left)
        print(node.val)
        preOrderTranversal(node.right)
        
def inOrderTranversal(node):
    if node is None:
        return 
    else:
        print(node.val)
        inOrderTranversal(node.left)
        inOrderTranversal(node.right)
        

class Sol:
    def solve(self, arr):
        head = builtBST(arr, 0, len(arr)-1)
        preOrderTranversal(head)
        inOrderTranversal(head)
        
            
sol = Sol()
print(sol.solve([1,2,3,4,5,6,7]))


ass = "01   0 0"
listv = ass.split(" ")
string = "".join(listv[::-1])
print(string)
print(listv)
num = 0 
