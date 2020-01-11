

import heapq

class Solution:
    def findNUglyNumber(self, primes, N):
        heap = []   
        next_idx = [0]*len(primes)
        ugly_numbers = []
        ugly_numbers.append(1)
        for i in range(len(primes)):
            heapq.heappush(heap, [primes[i], i])
        for i in range(2, N+1):
            number, idx =  heapq.heappop(heap)
            ugly_numbers.append(number)
            next_idx[idx] += 1 
            next_ele = ugly_numbers[next_idx[idx]]*primes[idx]
            heapq.heappush(heap, [next_ele,idx])
        return ugly_numbers[-1]

o_sol = Solution()
print(o_sol.findNUglyNumber([2,5],5))