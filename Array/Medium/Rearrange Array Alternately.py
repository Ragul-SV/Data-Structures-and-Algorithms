#---------------------------------METHOD1----------O(N^2)-----------------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    flag = 0
    index = 0
    for i in range(n-1):
        if not flag:
            max_ele = arr[i]
            index = i
            for j in range(i+1,n):
                if arr[j]>max_ele:
                    max_ele = arr[j]
                    index = j
            arr[i],arr[index]=arr[index],arr[i]
        else:
            min_ele = arr[i]
            index = i
            for j in range(i+1,n):
                if arr[j]<min_ele:
                    min_ele = arr[j]
                    index = j
            arr[i],arr[index]=arr[index],arr[i]
        flag = not flag
    for i in arr:
        print(i,end=" ")
    print()
#---------------------------------METHOD2--------O(N)---------------------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    min_index = 0
    max_index = n-1
    max_ele = arr[n-1]+1
    for i in range(n):
        if i%2==0:
            arr[i]+=(arr[max_index] % max_ele) * max_ele
            max_index-=1
        else:
            arr[i]+=(arr[min_index] % max_ele) * max_ele
            min_index+=1
    for i in arr:
        print(int(i/max_ele),end=" ")
    print()
