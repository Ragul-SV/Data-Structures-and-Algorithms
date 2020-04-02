for cases in range(t):
    st1 = input()
    st2 = input()
    d1 = dict()
    d2 = dict()
    for i in range(len(st1)):
        d1[st1[i]] = 1
    for i in range(len(st2)):
        d2[st2[i]] = 1
    l = []
    for i in d1.keys():
        if i not in d2:
            l.append(i)
    for i in d2.keys():
        if i not in d1:
            l.append(i)
    l.sort()
    for i in l:
        print(i,end="")
    print()
