t = int(input())
for cases in range(t):
    s = input()
    p = input()
    dp = dict()
    for i in range(len(p)):
        if p[i] not in dp:
            dp[p[i]] = 1
        else:
            dp[p[i]] += 1
    i = 0
    start = 0
    ds = dict()
    flag = 0
    c = 0
    while i<len(s):
        if s[i] not in dp:
            start = i+1
            ds = dict()
            flag = 0
        else:
            if flag==1:
                if s[start] in ds:
                    ds[s[start]]-=1
                    if ds[s[start]]==0:
                        del ds[s[start]]
                    start+=1
            if s[i] not in ds:
                ds[s[i]] = 1
            else:
                ds[s[i]] += 1
            if len(ds)==len(dp):
                if ds==dp:
                    c+=1
                    flag = 1
        i+=1
    print(c)
