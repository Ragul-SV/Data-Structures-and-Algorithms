t = int(input())
for cases in range(t):
    s = input()
    k = len(s)-1
    if int(s[k])==0:
        print(s)
    elif int(s[k])<=5:
        s = s[:k]+'0'
        print(s)
    elif int(s[k])>5:
        s = s[:k]+'0'
        flag = 1
        while k>=1 and flag==1:
            k-=1
            if int(s[k])<9:
                s = s[:k]+str(int(s[k])+1)+s[k+1:]
                print(s)
                flag = 0
            else:
                s = s[:k]+'0'+s[k+1:]
        if k==0 and flag==1:
            s = '1'+s
            print(s)
        
    
