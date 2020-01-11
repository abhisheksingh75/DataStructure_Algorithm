class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B, K):
        
        #keep first array as the smaller one
        if len(A) > len(B):
           return self.findMedianSortedArrays(B,A)
        
        n = len(A)
        m = len(B)
        low = 0
        high = min(len(A), K)
        
        while(low <=high):
            partitionX = (low + high)//2
            partitionY = K-partitionX
            while(partitionY>=m):
                partitionY -= 1
                partitionX += 1

            #calculate maxleftX
            if partitionX == 0:
                maxLeftX = -1*(1<<31)
            else:
                maxLeftX = A[partitionX-1]
            
            #calculate minRightX
            if partitionX >= n:
                minRightX = 1<<31
            else:
                minRightX = A[partitionX]
                
            #calculate minleftY
            if partitionY == 0:
                maxLeftY = -1*(1<<31)
            else:
                maxLeftY = B[partitionY-1]


            #calculate minRightY
            if partitionY >= m:
                minRightY = 1<<31
            else:
                minRightY = B[partitionY]
                
            #print("maxLeftX:"+str(maxLeftX)+"minRightX:"+str(minRightX))   
            #print("maxLeftY:"+str(maxLeftY)+"minRightY:"+str(minRightY)) 
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                    return float(max(maxLeftX,maxLeftY))
            elif maxLeftX > minRightY:
                high = partitionX-1
            else:
                low = partitionX+1
    
        return         
                
                
sol = Solution()
alpha = [[1,2],[0,2], [5,1],[3,3]]
A = [100, 112, 256, 349, 770]
alpha.sort(key = lambda x:( -1*x[1], x[0]))
print(alpha)
B = [72, 86, 113, 119, 265, 445, 892]
#print(sol.findMedianSortedArrays(A,B,1))
for i in range((len(A)+len(B))-1):
    print(sol.findMedianSortedArrays(A,B,i+1)) 
            
            
                        
