
class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None
    def insert_node_at_end(self, head, val):
        tmp =  head 
        while(tmp.next):
            tmp = tmp.next 
        tmp.next = Node(val)

class Solution:
    def solve(self, head):
        
        slow_ptr = head 
        fast_ptr = head 
        while(fast_ptr.next and fast_ptr.next.next):
            slow_ptr = slow_ptr.next 
            fast_ptr = fast_ptr.next.next 
        
        if fast_ptr.next:
            n = 2
        else:
            n = 3 
        #reverse half nodes
        prev = slow_ptr 
        curr = slow_ptr.next
        while(curr):
            tmp = curr.next 
            curr.next = prev
            prev = curr  
            curr = tmp 
            
        start_ptr = head 
        end_ptr = prev
        if n == 2:
            start_ptr = start_ptr.next 
            change_node = True
        else:
            change_node = False
        prev = None
        while(start_ptr!= end_ptr):
            if change_node == True:
                change_node = False 
                start_ptr.val, end_ptr.val = end_ptr.val, start_ptr.val
            else:
                change_node = True 
            tmp = end_ptr 
            end_ptr = end_ptr.next 
            start_ptr = start_ptr.next 
            tmp.next = prev 
            prev = tmp  
        if n == 2:
            end_ptr.next = prev 
        return head     
        
sol = Solution()
LL = Node('A')
LL.insert_node_at_end(LL, 'B')
LL.insert_node_at_end(LL, 'C')
LL.insert_node_at_end(LL, 'D')
"""
LL.insert_node_at_end(LL, 'E')
LL.insert_node_at_end(LL, 'F')
LL.insert_node_at_end(LL, 'G')
LL.insert_node_at_end(LL, 'H')
"""
new_ll = sol.solve(LL)
print("done")
list = []

while(new_ll):
    list.append(new_ll.val)
    new_ll = new_ll.next
print("->".join(list))
count = 5
return 1 if count < 0 else 0