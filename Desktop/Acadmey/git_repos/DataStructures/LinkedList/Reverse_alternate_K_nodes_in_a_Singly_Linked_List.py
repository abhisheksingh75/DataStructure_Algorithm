
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None



class Solution:
    
    def sol(self, head, k):
        if head is None:
            return None
        
        prev = None
        curr = head
        count = 0 
        while(count<k and curr):
            tmp = curr.next
            curr.next = prev 
            prev = curr
            curr = tmp 
            count += 1 
        head.next = self.sol(curr, k)
        return prev



LL = Node(1)
LL.next = Node(2)
LL.next.next = Node(3)
LL.next.next.next = Node(4)
LL.next.next.next.next = Node(5)
LL.next.next.next.next.next = Node(6)
LL.next.next.next.next.next.next = Node(7)
LL.next.next.next.next.next.next.next = Node(8)
LL.next.next.next.next.next.next.next.next = Node(9)
LL.next.next.next.next.next.next.next.next.next = Node(10)

o_bject  = Solution()
ll = o_bject.sol(LL, 10)
string = ""
while (ll):
    string = string+str(ll.val)+"->"
    ll = ll.next
print(string[:len(string)-2])