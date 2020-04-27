def nextPalindromeUtil(arr,n):
    mid = n//2
    leftsmaller = False
    i = mid-1
    j = mid+1 if n%2 else mid
    while i>=0 and arr[i]==arr[j]:
        i-=1
        j+=1
    if i<0 or arr[i]<arr[j]:
        leftsmaller = True
    while i>=0:
        arr[j] = arr[i]
        i-=1
        j+=1
    if leftsmaller:
        carry = 1
        i = mid-1
        if n%2:
            arr[mid] += carry
            carry = arr[mid]//10
            arr[mid]%=10
            j = mid+1
        else:
            j = mid
        while i>=0 and carry:
            arr[i] += carry
            carry = arr[i]//10
            arr[i]%=10
            arr[j] = arr[i]
            i-=1
            j+=1

def all9(arr,n):
    for i in range(n):
        if arr[i]!=9:
            return False
    return True

def nextPalindrome(arr,n):
    if all9(arr,n):
        print(1,end=" ")
        for i in range(1,n):
            print(0,end=" ")
        print(1)
    else:
        nextPalindromeUtil(arr,n)
        for i in range(n):
            print(arr[i],end=" ")
        print()

t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    nextPalindrome(arr,n)
