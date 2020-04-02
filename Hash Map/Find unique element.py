from collections import Counter
t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    c = Counter(arr)
    for i in c.elements():
        if c[i]==1:
            print(i)
