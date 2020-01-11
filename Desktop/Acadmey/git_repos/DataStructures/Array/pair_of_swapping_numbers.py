"""
Find a pair of elements swapping which makes sum of two arrays same
"""
from math import floor
from random import randrange, random
class Solution:
    def solve(self, arr):
        len_arr = len(arr)
        for i in range(len_arr-1, -1,-1):
            rand_idx = randrange(0, i+1)
            arr[i], arr[rand_idx] = arr[rand_idx], arr[i]
        return arr
            
        

sol = Solution()
arr = [1,2,3,4,5,6,7]
print(sol.solve(arr))

def f(n): #// counts how many 1's for number n
    out = 0;
    while(n!=0):
        out += (n % 10 == 1)
        n = n//10
    return out
print(f(25))