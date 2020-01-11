class DoubleLinkedList:
    def __init__(self, key):
        self.key = key 
        self.prev = None 
        self.next = None 

class Pair:
    def __init__(self, value, address):
        self.value = value 
        self.address  = address 
        
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity 
        self.head = None 
        self.tail = None 
        self.masterMap = {}
        

    # @return an integer
    def get(self, key):
        
        if key in self.masterMap:
            value = self.masterMap[key].value 
        else:
            return -1
        #update node position
        self.updateNodePos(self.masterMap[key].address) 
        return value 
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def put(self, key, value):
        #print(self.tail)
        #check if key is present in mastermap
        if key in self.masterMap:
            self.masterMap[key].value = value 
            self.updateNodePos(self.masterMap[key].address)
            return 
        if self.capacity == 0:
            tail_key = self.tail.key
            if self.tail != self.head:
                self.tail= self.tail.prev  
                self.tail.next = None 
            else:
                self.tail,self.head = None, None
            del self.masterMap[tail_key]
            self.capacity += 1
        
        self.insertValue(key,value)
        
        self.capacity -= 1
                
                
    
    #remove node in between and append to first
    def updateNodePos(self, node):
        if node == self.head:
            return 
        if node ==  self.tail:
            self.tail = self.tail.prev
        #get the node 
        if node.prev is not  None:
            node.prev.next = node.next
            
        if node.next is not None:
            node.next.prev = node.prev 
        
        #append node at first
        node.next = self.head
        node.prev = None 
        self.head.prev = node 
        self.head = node 
    
    def insertValue(self,key, value):
        new_node = DoubleLinkedList(key)
        
        #append new node to masterMap 
        self.masterMap[key] = Pair(value, new_node)
        
        #append this new node to list 
        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node
            self.tail.next = None 
        return 

def printLL(head, map):
    LL = []
    while(head):
        LL.append(str(map[head.key].value))
        head = head.next 
    print("->".join(LL))          
            
cache = LRUCache(1)

cache.put(2, 1)
print(cache.get(2))       #// returns 1
printLL(cache.head, cache.masterMap)
cache.put(3, 2)    #// evicts key 2
print(cache.get(2))       #// returns -1 (not found)
printLL(cache.head, cache.masterMap)
print(cache.get(3))#       // returns 3
printLL(cache.head, cache.masterMap)
        
        
        
        
