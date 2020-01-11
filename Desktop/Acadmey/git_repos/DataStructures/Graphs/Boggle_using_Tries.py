
def add_word_trie(word, head):
    tmp = head
    for i in range(len(word)):
        if word[i] in tmp.children:
            tmp = tmp.children[word[i]]
        else:
            new_node = Tries(word[i])
            tmp.children[word[i]] = new_node
            tmp  = new_node
    tmp.isTerminal = True
    return 
            
def create_trie(words):
    head =  Tries(None)
    for word in words:
        add_word_trie(word, head)
    return head

def isSafe(i,j,visited, lenc, lenr):
    
    if 0<=i<lenr and 0<=j<lenc and visited[i][j] == False:
        return True
    else:
        return False
    
def DFS(Boggle,head, i, j, visited, ans, str):
    lenc = len(Boggle[0])
    lenr = len(Boggle)
    rowNo = [-1,-1,-1,0,0,1,1,1]
    colNo = [-1,0,1,-1,1,-1,0,1]
    
    visited[i][j] = True
    str += Boggle[i][j]
    
    if head.isTerminal == True:
        ans.append(str)
        return 
    
    for k in range(8):
        if isSafe(i+rowNo[k], j+colNo[k], visited,lenc,lenr):
            if Boggle[i+rowNo[k]][j+colNo[k]] in head.children:
                DFS(Boggle,head.children[Boggle[i+rowNo[k]][j+colNo[k]]], i+rowNo[k], j+colNo[k], visited, ans, str)
                visited[i+rowNo[k]][j+colNo[k]] = True
    #visited[i,j] = False
        

class Tries:
    def __init__(self, ch):
        self.char = ch
        self.isTerminal = False
        self.children = {}


class BoggleSolver:
    
    def findWord(self, Boggle, words):
        head = create_trie(words)
        lenc =len(Boggle)
        lenr = len(Boggle[0])
        ans = []
        for i in range(lenc):
            for j in range(lenr):
                if Boggle[i][j] in head.children:
                    visited = [[False for j in range(lenc)] for i in range(lenr)]
                    DFS(Boggle,head.children[Boggle[i][j]], i, j, visited, ans, "")
                    
        return ans
                    
                    
o_object = BoggleSolver()
print(o_object.findWord([['G','O','Z'],['U','E','K'],['Q','S','E']], ["GEEKS", "FOR", "QUIZ", "GO"])) 
        