def counts(teamA, teamB):
    teamA.sort()
    d = dict()
    m = len(teamA)
    n = len(teamB)
    arr = [[teamB[i],i] for i in range(len(teamB))]
    arr = sorted(arr,key=lambda x:x[0])
    k = 0
    res = []
    for i in range(n):
        while k<m and teamA[k]<=arr[i][0]:
            k+=1
        if k<m:
            d[arr[i][0]] = k
        else:
            d[arr[i][0]] = m
    for i in range(n):
        res.append(d[teamB[i]])
    return res
