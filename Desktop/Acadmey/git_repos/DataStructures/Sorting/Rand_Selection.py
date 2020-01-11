import random
def partition(A, start, end):
    if start == end:
        return start
    pos = random.randrange(start,end)
    A[pos], A[end] = A[end], A[pos]   
    pivot_ele = A[end]
    i,j = start, end-1
    while(i<=j):
        
        if A[i] > pivot_ele:
            A[i], A[j] = A[j],A[i]
            j -= 1
        else:
            i += 1
    #print("end:"+str(end)+"i:"+str(i))
    A[end], A[i] = A[i], A[end]
    
    #print(A[i])
    return i
             
    

def quickSort(A, start, end, k):
    if start<=end:
        
        pivot = partition(A,start,end)
        if pivot == (k-1):
            return A[pivot]
        elif pivot > k-1:
            return quickSort(A,start,pivot-1, k)
        else:
            return quickSort(A,pivot+1,end, k)

arr = [6,3,7,9,8,1,2,0,-5,4,10,1,15,1,12]
for i in range(len(arr)):
    print(quickSort(arr, 0, len(arr)-1, i))


        