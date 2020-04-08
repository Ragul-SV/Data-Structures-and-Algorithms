#---------------------------------------------METHOD1-----------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    s = n*(n+1)//2
    print(s-sum(arr))
#---------------------------------------------METHOD2-----------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    s = 1
    for i in range(2,n+1):
        s+=i
        s-=arr[i-2]
    print(s)
#---------------------------------------------METHOD3-----------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    s1,s2 = 0,0
    for i in range(1,n+1):
        s1 = s1^i
    for i in range(n-1):
        s2 = s2^arr[i]
    print(s1^s2)
