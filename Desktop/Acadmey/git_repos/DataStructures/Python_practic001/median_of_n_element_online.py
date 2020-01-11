import heapq
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        left_max_heap = []
        right_min_heap = []
        for ele in A:
            
            if (len(left_max_heap) == 0 or ele <(-1*left_max_heap[0])):
                heapq.heappush(left_max_heap, -1*ele)
            else:
                heapq.heappush(right_min_heap, ele)
            
            while(abs(len(left_max_heap)-len(right_min_heap))>1):
                
                if len(left_max_heap) < len(right_min_heap):
                    heapq.heappush(left_max_heap, -1*heapq.heappop(right_min_heap))
                else:
                    heapq.heappush(right_min_heap, -1*heapq.heappop(left_max_heap))
            
            print("left_max_heap:"+str(left_max_heap))
            print("right_min_heap:"+str(right_min_heap))
            if  (len(left_max_heap) + len(right_min_heap))%2 == 0:
                 ans.append(-1*left_max_heap[0])
            else:
                if len(left_max_heap) > len(right_min_heap):
                    ans.append(-1*left_max_heap[0])
                else:
                    ans.append(right_min_heap[0])
            
        return ans
                    

o_object = Solution()
print(o_object.solve([5, 17, 100, 11]))