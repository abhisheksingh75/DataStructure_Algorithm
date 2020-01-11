#code
def findMissingNumber(arr):
    
    i = 0 
    while(i<len(arr)):
        print(arr)
        if arr[i] == i+1 or arr[i] <= 0  or arr[i] > len(arr):
            i += 1
        else:
            tmp = arr[i]
            arr[i] = arr[tmp-1]
            arr[tmp-1] = tmp

    for i in range(len(arr)):
        if arr[i] != i+1:
            return i+1 
    return len(arr)
    
    
testcases = int(input())
for i in range(testcases):
    size = input()
    arr = list(map(int, input().strip().split()))
    print(findMissingNumber(arr))