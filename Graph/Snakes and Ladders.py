class Queue:
    def __init__(self,v=0,dist=0):
        self.v = v
        self.dist = dist

def minstep(move):
    visited = [False]*30
    q = []
    visited[0] = True
    q.append(Queue(0,0))
    while q:
        qtemp = q.pop(0)
        if qtemp.v == 29:
            break
        j = qtemp.v + 1
        while j<=qtemp.v+6 and j<30:
            if visited[j] == False:
                qt = Queue()
                qt.v = move[j] if move[j]!=-1 else j
                qt.dist = qtemp.dist + 1
                q.append(qt)
                visited[j] = True
            j+=1
    return qtemp.dist
    
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    move = [-1]*30
    for i in range(0,2*n,2):
        move[arr[i]-1] = arr[i+1]-1
    print(minstep(move))
