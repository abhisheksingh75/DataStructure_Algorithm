''' This is a function problem.You only need to complete the function given below '''
# your task is to complete this function
# function should return index to the any valid peak element
def addPolynomial(poly1, poly2):
    head = poly1
    prev= None
    # Code here
    if poly1.power<poly2.power:
        #print("recurse")
        return addPolynomial(poly2,poly1)
        

    while(poly1 is not None and poly1.power>poly2.power):
        #print("A")
        prev = poly1
        poly1 = poly1.next
    while(poly1 is not None and poly2 is not None):
        poly1.coef = poly1.coef + poly2.coef
        prev = poly1
        poly1 = poly1.next
        poly2 = poly2.next
    if poly2 is not None:
        prev.next = poly2 
    ans_list = []
    while(head is not None):
        term = ""
        term += str(head.coef)
        if head.power != 0:
            term += "x^"
            term +=  str(head.power)
        ans_list.append(term)
        head = head.next
    return "+".join(ans_list)


# Node Class    
class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
    def insert(self, coeff, pwr):
        if self.head == None:
            self.head = node(coeff, pwr)
        else:
            new_node = node(coeff, pwr)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node
def createList(arr, n):
    lis = Linked_List()
    k=0
    for i in range(n):
        lis.insert(arr[k], arr[k+1])
        k+=2
    return lis.head
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        poly1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        poly2 = createList(arr, n)
        print(addPolynomial(poly1, poly2))
# Contributed by: Harshit Sidhwa

