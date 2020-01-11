#Initial Template for Python 3
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
        
                  
def addNode(head, curr_node, ptr):
    
    if head is None:
        head = ptr
        curr_node = ptr
    else:
        curr_node.bottom = ptr
        curr_node = curr_node.bottom
    return 
def flatten(root):
    #Your code here
    node = root 
    if node.next is None:
        return node 
    else:
        ptr1 = node 
        ptr2 = flatten(node.next)
        head, curr_node = None, None 
        while(ptr1 is not None and ptr2 is not None):
            if ptr1.data < ptr2.data:
                addNode(head, curr_node, ptr1)
                ptr1 = ptr1.bottom
            else:
                addNode(head, curr_node, ptr2)
                ptr2 = ptr2.bottom
        if ptr1 is not None:
            if curr_node is not None:
                curr_node.bottom = ptr1
        elif ptr2 is not None:
            if curr_node is not None:
                curr_node.bottom = ptr2
        return head
            
            
            
            

def printList(node):
    while(node is not None):
        print(node.data,end=" ")
        node=node.bottom
        
    print()
if __name__=="__main__":
    t=int(input())
    while(t>0):
        head=None
        N=int(input())
        arr=[]
        
        arr=[int(x) for x in input().strip().split()]
        temp=None
        tempB=None
        pre=None
        preB=None
        
        flag=1
        flag1=1
        listo=[int(x) for x in input().strip().split()]
        it=0
        
        for i in range(N):
            m=arr[i]
            m-=1
            a1=listo[it]
            it+=1
            temp=Node(a1)
            if flag is 1:
                head=temp
                pre=temp
                flag=0
                flag1=1
            else:
                pre.next=temp
                pre=temp
                flag1=1
                
            for j in range(m):
                a=listo[it]
                it+=1
                tempB=Node(a)
                if flag1 is 1:
                    temp.bottom=tempB
                    preB=tempB
                    flag1=0
                else:
                    preB.bottom=tempB
                    preB=tempB
        root=flatten(head)
        printList(root)
        
        t-=1
