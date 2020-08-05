def find(l,n,index):
    global ans
    if(n==1):
        ans=ans+1
        return
    elif(n<1):
        return
    i=index
    while(i<len(l)):
        if(n%l[i]==0):
            find(l,n/l[i],i)
        i=i+1

ans=0    
def getFactors(n):
    global ans
    l=list()
    ans=0 
    
    if(n==1):
        return ans
    
    i=2
    
    while(i*i<=n):
        if(n%i==0):
            if(n//i==i):
                l.append(i)
            else:
                l.append(i)
                l.append(n//i)
        i=i+1
    
    l.sort()
    find(l,n,0)
    
    return ans
