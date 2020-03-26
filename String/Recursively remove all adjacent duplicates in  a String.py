def duplicate(st,i,res):
    if i==len(st):
        flag = True
        for j in range(len(res)-1):
            if res[j]==res[j+1]:
                flag = False
        if flag:
            return res
        else:
            return duplicate(res,0,"")
    if ((i+1)<=(len(st)-1) and st[i]==st[i+1]) or ((i-1)>=0 and st[i]==st[i-1]):
        return duplicate(st,i+1,res)
    else:
        res+=st[i]
        return duplicate(st,i+1,res)

t = int(input())
for cases in range(t):
    st = input()
    res = ""
    print(duplicate(st,0,res))
