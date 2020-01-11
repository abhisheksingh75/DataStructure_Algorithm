

class Heapq:
    @staticmethod
    def heappush(heap,ele):
        heap.append(ele)
        lenHeap = len(heap)
        currpos = lenHeap-1
        while(currpos>0):
            if (currpos-1)//2 >= 0:
                if heap[(currpos-1)//2] > heap[currpos]:
                    heap[(currpos-1)//2],heap[currpos] = heap[currpos],heap[(currpos-1)//2]
                    currpos = (currpos-1)//2
                    continue
                else:
                    break
        return 

    @staticmethod        
    def heappop(heap):
        
        heap[0], heap[len(heap)-1] = heap[len(heap)-1],heap[0]
        ele = heap.pop()
        lenHeap = len(heap)
        currPos = 0
        while(currPos<lenHeap):
            
            if 2*currPos+1<lenHeap and 2*currPos+2<lenHeap:
                if heap[currPos] <= min(heap[2*currPos+1],heap[2*currPos+2]):
                    break
                elif heap[2*currPos+1]<=heap[2*currPos+2]:
                    heap[currPos],heap[2*currPos+1]= heap[2*currPos+1],heap[currPos]
                    currPos = 2*currPos+1
                    continue
                else:
                    heap[currPos],heap[2*currPos+2]= heap[2*currPos+2],heap[currPos]
                    currPos = 2*currPos+1
                    continue
            elif 2*currPos+1<lenHeap:
                if heap[currPos] <= heap[2*currPos+1]:
                    break 
                else:
                    heap[currPos],heap[2*currPos+1]= heap[2*currPos+1],heap[currPos]
                    currPos = 2*currPos+1
                    continue
            #if left child doesn't exist there won't be any right child
            else:
                break
        return ele

class Solution:
    
    def solve(self,A):
        heap = []
        for ele in A:
            print(heap)
            Heapq.heappush(heap, ele)
        print(heap)
        for i in range(6):
            print(Heapq.heappop(heap))
        print(heap)

o_object = Solution()   
o_object.solve([5,7,2,6,8,1])
