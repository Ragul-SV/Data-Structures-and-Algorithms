import math
t = int(input())
for cases in range(t):
    n = int(input())
    s = input()
    d = dict()
    for i in range(n):
        if s[i] in d:
            d[s[i]]+=1
        else:
            d[s[i]] = 1
    c = 0
    for i in d.keys():
        c+=((d[i]*(d[i]+1))/2)
    print(int(c))
