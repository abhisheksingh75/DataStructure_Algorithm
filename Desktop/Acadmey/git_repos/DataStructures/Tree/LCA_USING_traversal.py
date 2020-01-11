
class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right  = None 

def findNodePath(node, node_val, ans, tmp):
    if node:
        if node.val == node_val:
            tmp.append(node.val)
            ans.extend(tmp[:]) 
            return 
        tmp.append(node.val)
        findNodePath(node.left, node_val, ans, tmp)
        findNodePath(node.right, node_val, ans, tmp)
        tmp.pop()
        return 

class Solution:
    def solve(self, head, node1_val, node2_val):
        path1 = []
        findNodePath(head,node1_val, path1, [])
        path2 = [] 
        findNodePath(head,node2_val, path2, [])
        print(path1)
        print(path2)
        if len(path1) >= 1 and len(path2) >= 1:
            for i in range(min(len(path1), len(path2))):
                if path1[i] == path2[i]:
                    ans = path1[i]
                else:
                    break
            return ans 
        else:
            return -1
        
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7)

sol = Solution()
print(sol.solve(root, 5, 8)) 