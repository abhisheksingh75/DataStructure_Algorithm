
def builtSegTree(A, seg_tree, start, end, tidx):
    if start ==  end:
        seg_tree[tidx] = 1
    else:
        mid = (start + end)//2
        builtSegTree(A, seg_tree, start, mid, 2*tidx+1)
        builtSegTree(A, seg_tree, mid+1, end, 2*tidx+2)
        seg_tree[tidx] = seg_tree[2*tidx+1] + seg_tree[2*tidx+2]
        return 
        
    
def seg_tree_find(A, seg_tree, start, end, tidx, value):
    if start == end:
       seg_tree[tidx] = 0
       return start
    else:
        mid  = (start +end )//2 
        if seg_tree[2*tidx+1]>=value:
            return_value = seg_tree_find(A,seg_tree,start, mid,2*tidx+1,value)
        else:
            return_value = seg_tree_find(A,seg_tree,mid+1,end,2*tidx+2,value-seg_tree[2*tidx+1])
        seg_tree[tidx] = seg_tree[2*tidx+1] + seg_tree[2*tidx+2]
    return return_value

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, A, B):
        ans = [-1]*len(A)
        N = len(A)
        seg_tree  = [0]*(4*len(A))
        heights_infornts = zip(A,B)
        heights_infornts = sorted(heights_infornts,key = lambda x:x[0])
        builtSegTree(A,seg_tree,0,len(A)-1,0)
        for height, infront in heights_infornts:
            ans[seg_tree_find(A,seg_tree, 0, N-1, 0, infront+1)] = height
        return ans

o_object = Solution()
print(o_object.order([5,3,2,6,1,4],[0,1,2,0,3,2]))
        
        
        