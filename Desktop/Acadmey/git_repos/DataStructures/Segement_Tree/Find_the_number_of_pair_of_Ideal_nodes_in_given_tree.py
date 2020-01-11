from collections import defaultdict 

def Add_Edge(a,b):
    graph[a].append(b)

def update_seg_tree(seg_tree, seg_idx, start, end, pos, val):
    #print("seg_idx:"+str(seg_idx)+"start:"+str(start)+"end:"+str(end)+"pos:"+str(pos)+"val:"+str(val))
    if start == end and start == pos:
        seg_tree[seg_idx] = val 
        return
    elif start > end:
        return 
    else:
        mid = (start+end)//2
        if mid >=pos:
            update_seg_tree(seg_tree, 2*seg_idx, start, mid, pos, val)
        else:
            update_seg_tree(seg_tree, 2*seg_idx+1, mid+1,end,pos,val)
        seg_tree[seg_idx] = seg_tree[2*seg_idx]+seg_tree[2*seg_idx+1]
        return 

def find_seg_tree(seg_tree,seg_idx, start, end, rleft, rright):
    #print("seg_idx:"+str(seg_idx)+"start:"+str(start)+"end:"+str(end)+"rleft:"+str(rleft)+"rright:"+str(rright))
    if rright<start or rleft > end:
        return 0 
    elif (rleft <= start and rright>=end):
        return seg_tree[seg_idx]
    else:
        mid = (start+end)//2
        left_val = find_seg_tree(seg_tree, 2*seg_idx, start, mid,rleft, rright)
        right_val = find_seg_tree(seg_tree, 2*seg_idx+1, mid+1, end,rleft, rright)
        return left_val+right_val
    
    
    
    
def DFS(node, visited, n,k, graph,seg_tree):
    
    
    if (node-k) <1:
        rleft  = 1
    else:
        rleft = node-k 
    
    if (node+k) > n:
        rright = n 
    else:
        rright = node+k
    print(seg_tree)
    print("rleft:"+str(rleft)+"rright:"+str(rright))
    DFS.ans += find_seg_tree(seg_tree,1, 1, n, rleft, rright)
    update_seg_tree(seg_tree, 1, 1, n, node, 1)
    print("node:"+str(node)+"ANS:"+str(DFS.ans))
    for child in graph[node]:
        DFS(child, visited, n,k, graph,seg_tree)
        update_seg_tree(seg_tree, 1, 1, n, child, 0)
    
    return 

class Sol:
    def solve(self,n, graph, k):
        seg_tree =  [0]*(4*(n+1))
        visited = [0]*(n+1)
        for parent in graph:
            for child in graph[parent]:
                visited[child] = 1
                
        for i in range(1, n+1):
            if visited[i] != 1:
                root = i 
                break 
        visited = [0]*(n+1)
        DFS.ans = 0
        DFS(root, visited, n, k, graph,seg_tree)
        return DFS.ans
                
        
        

sol = Sol()
        
graph = defaultdict(list)
#Add edges 
Add_Edge(1, 2) 
Add_Edge(1, 3) 
Add_Edge(3, 4) 
Add_Edge(3, 5) 
Add_Edge(3, 6) 
print(sol.solve(6,graph,3))
