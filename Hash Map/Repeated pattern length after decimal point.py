def findRepeat(p,q):
    p = abs(p)
    q = abs(q)
    rem = p%q
    if rem==0:
        return 0
    res = 0
    d = dict()
    d[rem] = 0
    while True:
        i = 0
        while rem<q:
            if i==0:
                rem = 10*rem
            else:
                rem = 10*rem
                res+=1
            i+=1
        rem = rem%q
        res+=1
        if rem not in d:
            d[rem] = res
        else:
            return res-d[rem]
        if rem==0:
            return 0
