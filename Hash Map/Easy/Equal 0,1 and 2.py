t = int(input())
for cases in range(t):
    s = input()
    d = dict()
    d["0*0"] = 1
    z,o,t = 0,0,0
    count = 0
    for i in range(len(s)):
        if s[i]=='0':
            z+=1
        if s[i]=='1':
            o+=1
        if s[i]=='2':
            t+=1
        temp = str(z-o)+'*'+str(z-t)
        if temp not in d:
            d[temp] = 1
        else:
            count += d[temp]
            d[temp]+=1
    print(count)
