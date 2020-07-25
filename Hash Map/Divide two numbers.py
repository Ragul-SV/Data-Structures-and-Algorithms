def divide(n,d):
    if n==0:
        return 0
    sign = -1 if (n<0)^(d<0) else 1
    n = abs(n)
    d = abs(d)
    res = ""
    if sign==-1:
        res+="-"
    res+=str(n//d)
    if n%d==0:
        return res
    res+="."
    rem = n%d
    i = 0
    mp = dict()
    repeating = False
    while rem>0 and not repeating:
        if rem in mp:
            i = mp[rem]
            repeating = True
            break
        else:
            mp[rem] = len(res)
        rem = rem*10
        res+=str(rem//d)
        rem = rem%d
    if repeating:
        res = res[:i]+'('+res[i:]+')'
    return res

n = int(input())
d = int(input())
print(divide(n,d))
