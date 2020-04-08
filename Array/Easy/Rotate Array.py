#---------------------------------------------------METHOD1-------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    arr = arr[k:]+arr[:k]
    for i in arr:
        print(i,end=" ")
    print()
#---------------------------------------------------METHOD2------------------------------------------------------------------#
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
        
def leftRotate(arr,n,k):
    for i in range(gcd(n,k)):
        temp = arr[i]
        j = i
        while True:
            d = j+k
            if d>=n:
                d-=n
            if d==i:
                break
            arr[j] = arr[d]
            j = d
        arr[j] = temp
    
t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    leftRotate(arr,n,k)
    for i in arr:
        print(i,end=" ")
    print()
