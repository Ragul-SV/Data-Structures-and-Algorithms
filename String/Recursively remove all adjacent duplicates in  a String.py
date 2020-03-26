def duplicate(st,i,res):
    if i==len(st):
        return res
    if ((i+1)<=(len(st)-1) and st[i]==st[i+1]) or ((i-1)>=0 and st[i]==st[i-1]):
        return duplicate(st,i+1,res)
    else:
        res+=st[i]
        return duplicate(st,i+1,res)

t = int(input())
for cases in range(t):
    st = input()
    res = ""
    flag = True
    for j in range(len(st)-1):
        if st[j]==st[j+1]:
            flag = False
    if flag==True:
        print(st)
    while flag==False:
        res = duplicate(st,0,res)
        flag = True
        for j in range(len(res)-1):
            if res[j]==res[j+1]:
                flag = False
        if flag==True:
            print(res)
            break
        else:
            st = str(res)
            res = ""
