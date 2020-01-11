from collections import deque

class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TreeOperation:
    
    def serialize(self, node):
        if node is None:
            return "$"
        
        else:
            leftTree = self.serialize(node.left)
            rightTree = self.serialize(node.right)
        return str(node.val) +","+leftTree+","+rightTree
    def deserialize(self, que_ele):
        ele = que_ele.popleft()
        if ele == "$":
            return None
        else:
            node = Node(ele)
            node.left = self.deserialize(que_ele)
            node.right = self.deserialize(que_ele)
        return node


Tree = Node(1)
Tree.left = Node(2)
Tree.right = Node(3)

Tree.left.left = Node(4)
Tree.left.right = Node(6)

Tree.left.right.left = Node(7)

Tree.right.right = Node(10)

o_object = TreeOperation()
print(o_object.serialize(Tree))
string = o_object.serialize(Tree)
que = deque()
list_ele = string.split(',')
[que.append(ele) for ele in list_ele]
deserialize_tree = o_object.deserialize(que)
print(deserialize_tree)


