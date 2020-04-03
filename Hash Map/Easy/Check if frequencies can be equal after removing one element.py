#------------------------------------------------------METHOD1------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    s = input()
    d = dict()
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    s = list(d.values())
    d.clear()
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    if (len(d)==1 and s[0]==1) or (len(d)==1 and len(s)==1):
        print(1)
    elif len(d)==2:
        l = list(d.keys())
        if l[1]-l[0]==1 and (d[l[1]]==1 or d[l[0]]==1):
            print(1)
        else:
            print(0)
    else:
        print(0)
#-----------------------------------------------------METHOD2-----------------------------------------------------------------#
t = int(input())
for cases in range(t):
    s = input()
    d = dict()
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    s = list(d.values())
    min_value = min(s)
    max_value = max(s)
    if (all(s[0]==ele for ele in s)==True or \
        (s.count(max_value)==len(s)-1) or \
        ((s.count(min_value)==len(s)-1) and (max_value-min_value)==1)):
            print(1)
    else:
        print(0)
