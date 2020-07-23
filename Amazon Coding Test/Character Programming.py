def getMaxDeletions(s):
    d = [0,0,0,0]
    for i in s:
        if i == 'U':
            d[0]+=1
        elif i == 'D':
            d[1]+=1
        elif i == 'L':
            d[2]+=1
        elif i == 'R':
            d[3]+=1
    return min(d[0],d[1])*2 + min(d[2],d[3])*2
