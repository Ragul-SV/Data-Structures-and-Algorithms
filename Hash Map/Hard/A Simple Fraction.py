t = int(input())
for cases in range(t):
    n = int(input())
    d = int(input())
    print(int(n/d),end="")
    hmap = dict()
    k = n%d
    if k==0:
        print()
        continue
    i = 0
    start = -1
    hmap[k] = i
    i+=1
    while True:
        k = (k*10)%d
        if k==0:
            break
        if k in hmap:
            start = hmap[k]
            break
        hmap[k] = i
        i+=1
    print('.',end="")
    for key,value in sorted(hmap.items(),key=lambda x:x[1]):
        if hmap[key]==start:
            print('(',end="")
        print(int(key*10/d),end="")
    if start>-1:
        print(')')
    else:
        print()
