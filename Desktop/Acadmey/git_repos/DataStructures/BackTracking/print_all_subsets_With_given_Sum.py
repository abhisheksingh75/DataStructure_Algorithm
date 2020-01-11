
def printAllSubsets(A,start, sum, res, tmp):
    
    if sum == 0:
        res.append(tmp[:])
    elif sum < 0:
        return
    else:
        for i in range(start, len(A)):
            tmp.append(A[i])
            printAllSubsets(A, i+1, sum-A[i],res,tmp)
            tmp.pop()
            

class Sol:
    def solve(self, set, sum):
        res = []
        printAllSubsets(set,0,sum,res,[])
        return res


o_object = Sol()
print(o_object.solve([3, 34, 4, 12, 5, 2], 9))
        