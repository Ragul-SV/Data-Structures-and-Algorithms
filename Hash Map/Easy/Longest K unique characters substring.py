t = int(input())
for cases in range(t):
    s = input()
    k = int(input())
    d = dict()
    c = 0
    maxlen = 0
    j = 0
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
            c+=1
        else:
            d[s[i]]+=1
        while c>k:
            d[s[j]]-=1
            if d[s[j]]==0:
                del d[s[j]]
                c-=1
                j+=1
                break
            j+=1
        if c==k:
            maxlen = max(maxlen,i-j+1)
    if maxlen==0:
        print(-1)
    else:
        print(maxlen)
        
        
