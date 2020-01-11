
def merge_interval(intervals):
    ans = []
    print(intervals)
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1,len(intervals)):
        if  start<=intervals[i][0]<=end:
            end = max(intervals[i][1], end)
        else:
            ans.append([start,end])
            start = intervals[i][0]
            end = intervals[i][1]
    ans.append([start,end])
    return ans 
class Solution:
    def insert(self, intervals, new_interval):
        if len(intervals) == 0:
            return [new_interval]
        elif new_interval[1]<intervals[0][0]:
            return [new_interval]+intervals
        elif new_interval[0]>intervals[len(intervals)-1][1]:
            return intervals+[new_interval]
        elif new_interval[0]<intervals[0][0] and new_interval[1]>intervals[len(intervals)-1][1]:
            return [new_interval]
        else:
            for i in range(len(intervals)):
                if intervals[i][0] >= new_interval[0]:
                    return merge_interval(intervals[:i]+[new_interval]+intervals[i:])
            return merge_interval(intervals+[new_interval])

        
sol = Solution()
#print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(sol.insert([[1,3],[6,9]], [2,5]))
#print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [18,34]))