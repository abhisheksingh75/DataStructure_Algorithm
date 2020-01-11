import random
def partition(A, start, end):
        
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
             
    

def quickSort(A, start, end):
    if start<end:
        
        pivot = partition(A,start,end)
        quickSort(A,start,pivot-1)
        quickSort(A,pivot+1,end)

arr = [6,3,7,9,8,1,2,0,-5,4,10,1,15,1,12]
quickSort(arr, 0, len(arr)-1)
print(arr)


        