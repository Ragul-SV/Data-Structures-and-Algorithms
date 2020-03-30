class Point:
    def __init__(self,x,y,time):
        self.x = x
        self.y = y
        self.time = time
    
def safe(x,y,m,n):
    if x>=0 and x<m and y>=0 and y<n:
        return True
    return False
    
def BFS(arr,m,n):
    q = []
    ftime = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j]==2:
                p = Point(i,j,0) 
                q.append(p)
    while q:
        temp = q[0]
        x = temp.x
        y = temp.y
        time = temp.time
        ftime = max(ftime,time)
        if safe(x-1,y,m,n) and arr[x-1][y]==1:
            p = Point(0,0,0)
            p.x = x-1
            p.y = y
            p.time = time+1
            arr[x-1][y] = 2
            q.append(p)
        if safe(x+1,y,m,n) and arr[x+1][y]==1:
            p = Point(0,0,0)
            p.x = x+1
            p.y = y
            p.time = time+1
            arr[x+1][y] = 2
            q.append(p)
        if safe(x,y-1,m,n) and arr[x][y-1]==1:
            p = Point(0,0,0)
            p.x = x
            p.y = y-1
            p.time = time+1
            arr[x][y-1] = 2
            q.append(p)
        if safe(x,y+1,m,n) and arr[x][y+1]==1:
            p = Point(0,0,0)
            p.x = x
            p.y = y+1
            p.time = time+1
            arr[x][y+1] = 2
            q.append(p)
        q.pop(0)
    return ftime

t = int(input())
for case in range(t):
    m,n = map(int,input().strip().split())
    l = list(map(int,input().strip().split()))
    arr = []
    k = 0
    for i in range(m):
        b = []
        for j in range(n):
            b.append(l[k])
            k+=1
        arr.append(b)
    res = BFS(arr,m,n)
    for i in range(m):
        for j in range(n):
            if arr[i][j]==1:
                res = -1
                break
    print(res)
