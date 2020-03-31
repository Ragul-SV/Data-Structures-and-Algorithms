def isSafe(x,y,n):
    return x>=1 and x<=n and y>=1 and y<=n

t = int(input())
for cases in range(t):
    n = int(input())
    x1, y1 = map(int,input().strip().split())
    x2, y2 = map(int,input().strip().split())
    dp = []
    for i in range(n+1):
        b = []
        for j in range(n+1):
            b.append(2**31)
        dp.append(b)
    dx = [2,2,-2,-2,1,1,-1,-1]
    dy = [1,-1,1,-1,2,-2,2,-2]
    q = [[x1,y1]]
    count = 0
    while q:
        s = len(q)
        flag = 0
        for i in range(s):
            temp = q.pop(0)
            for j in range(8):
                x = temp[0] + dx[j]
                y = temp[1] + dy[j]
                if isSafe(x,y,n):
                    if count+1<dp[x][y]:
                        flag = 1
                        dp[x][y] = count+1
                        q.append([x,y])
        if flag:
            count+=1
    if x1==x2 and y1==y2:
        dp[x2][y2] = 0
    
    if dp[x2][y2]==2**31:
        dp[x2][y2] = 1
    
    print(dp[x2][y2])
    
