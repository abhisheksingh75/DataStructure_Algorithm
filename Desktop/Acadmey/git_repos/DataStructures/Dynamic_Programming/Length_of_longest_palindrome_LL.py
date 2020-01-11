
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def lenOfPalindrome(node1, node2):
    length = 0
    
    while(node1 and node2):
        if node1.val == node2.val:
            length += 2
            node1 = node1.next
            node2 = node2.next
        else:
            return length
    return length

class Solution:
    
    def sol(self, head):
        
        prev= None
        curr = head
        max_len = 0
        while(curr is not None):
            print(curr.val)
            tmp = curr.next
            curr.next = prev 
            even_len = 0
            #print("curr:"+str(curr.val)+"tmp:"+str(tmp.val))
            #consider even length palindrome
            even_len = lenOfPalindrome(curr, tmp)
            odd_len = 0
            #if prev is not None:
            #    print("prev:"+str(prev.val))
            #consider odd length palindrome 
            odd_len = lenOfPalindrome(prev, tmp) + 1
            
            max_len = max(max_len,odd_len,even_len)
            
            prev = curr
            curr = tmp
            
            
        return max_len



LL = Node(2)
LL.next = Node(1)
LL.next.next = Node(2)
LL.next.next.next = Node(1)
LL.next.next.next.next = Node(2)
LL.next.next.next.next.next = Node(2)
LL.next.next.next.next.next.next = Node(1)
LL.next.next.next.next.next.next.next = Node(3)
LL.next.next.next.next.next.next.next.next = Node(2)
LL.next.next.next.next.next.next.next.next.next = Node(2)

o_bject  = Solution()
print(o_bject.sol(LL))

    
    