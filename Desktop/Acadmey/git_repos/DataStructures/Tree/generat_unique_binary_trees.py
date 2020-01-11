class Node:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 

def inOrder(root):
    #print(root)
    stack = []
    curr = root 
    ans = []
    while(curr or stack):
        if (curr):
            stack.append(curr)
            curr = curr.left 
            continue 
        if stack:
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
            
    return ans[:] 

def genBinaryTree(start, end):
    list = []
    if start == end:
        list.append(Node(start))
        return list[:]
    elif  start > end:
        list.append(None)
        return list[:]
    else:
        for i in range(start, end+1):
            left = genBinaryTree(start, i-1)
            right = genBinaryTree(i+1, end)
            #print("left:"+str(left))
            #print("right:"+str(right))
            for left_val in range(len(left)):
                for right_val in range(len(right)):
                    root = Node(i)
                    root.left = left[left_val]
                    root.right = right[right_val]
                    list.append(root) 
        
        #print("start:"+str(start)+"end:"+str(end)+"list:"+str(list))
        return list[:] 
class Solution:
    def solve(self, n):
        return genBinaryTree(1, n)
        
sol = Solution()
list = sol.solve(3)
for i in range(len(list)):
    print(inOrder(list[i]))
