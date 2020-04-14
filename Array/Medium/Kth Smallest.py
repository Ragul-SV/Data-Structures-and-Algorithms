#---------------------METHOD--------O(N)-TO-O(N^2)-----------------------------------------------------------------------------------#
def kthsmallest(arr,l,r,k):
    if k>0 and k<=r-l+1:
        n = r-l+1
        pivot = int(random.random() % n)
        arr[l+pivot],arr[r] = arr[r],arr[l+pivot]
        pos = partition(arr,l,r)
        if pos-l==k-1:
            return arr[pos]
        elif pos-l>k-1:
            return kthsmallest(arr,l,pos-1,k)
        else:
            return kthsmallest(arr,pos+1,r,k-pos+l-1)
    else:
        return -1
        
def partition(arr,l,r):
    temp = arr[r]
    i = l
    for j in range(l,r):
        if arr[j]<=temp:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    arr[i],arr[r] = arr[r],arr[i]
    return i
            

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        k = int(input())
        print(kthsmallest(arr,0,n-1,k))
