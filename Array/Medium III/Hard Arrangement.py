def arrange(a,b,n):
    l = [[a[i],b[i]] for i in range(n)]
    l.sort(key = lambda k:(-1*k[0],k[1]))
    res = []
    for i in range(n):
        res.insert(l[i][1],l[i][0])
    return res
