#code

def biTreeGetSum(biTree, idx):
    prefix_sum = 0 
    while(idx>0):
        prefix_sum += biTree[idx]
        idx = idx - (idx&(-1*idx))
    return prefix_sum

def biTreeUpdate(biTree, idx, val):
    
    while(idx<=len(biTree)-1):
        biTree[idx] += val 
        idx = idx + (idx&(-1*idx))
    return 
    
def cntMagicTriplets(inp_list):
    max_ele = max(inp_list)
    biTree = [0]*(max_ele+1)
    count_inversions = 0 
    smaller = [0]*len(inp_list)
    bigger = [0]*len(inp_list)
    for i in range(len(inp_list)):
        number = biTreeGetSum(biTree,inp_list[i]-1)
        smaller[i] = number 
        biTreeUpdate(biTree, inp_list[i], 1)
    #print(smaller)
    biTree = [0]*(max_ele+1)
    #print(biTree)
    for i in range(len(inp_list)-1, -1, -1):
        number = biTreeGetSum(biTree,inp_list[i])
        bigger[i] = len(inp_list)-i-1-number 
        biTreeUpdate(biTree, inp_list[i], 1)
        #print(biTree)
        #print("bigger[i]:"+str(bigger[i])+"A[i]:"+str(inp_list[i]))
    #print(bigger)
    for i in range(len(inp_list)):
        count_inversions += (smaller[i]*bigger[i])
    return count_inversions
testcases = int(input())
for i in range(testcases):
    inp_len = input()
    inp_list = list(map(int, input().strip().split()))
    print(cntMagicTriplets(inp_list))
    
"""
84
47 10 20 30 32 11 73 58 74 3 20 63 68 84 71 25 79 17 17 60 57 76 10 3 27 27 56 44 20 6 43 67 55 18 52 2 29 80 59 58 82 34 36 21 74 63 45 24 79 18 83 8 9 9 10 75 75 65 74 10 70 33 76 81 6 83 82 74 78 13 4 31 46 39 52 75 57 52 15 8 25 13 15 33
"""
