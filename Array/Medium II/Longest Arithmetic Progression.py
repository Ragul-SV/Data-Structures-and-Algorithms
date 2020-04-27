#------------------------------METHOD1--------------------------------#
def longestAP(arr,n):
    if n<=2:
        return n
    llap = 2
    d = [dict()]*n
    for i in range(1,n):
        for j in range(0,i):
            diff = arr[i] - arr[j]
            if diff in d[j]:
                d[i][diff] = 1+d[j][diff] 
            else:
                d[i][diff] = 2
            llap = max(llap,d[i][diff])
    return llap

t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    print(longestAP(arr,n))
#-----------------------------METHOD2---------------------------------#
def lenghtOfLongestAP(set, n): 
    if (n <= 2): 
        return n  
    L = [[0 for x in range(n)] 
            for y in range(n)] 
    llap = 2

    for i in range(n): 
        L[i][n - 1] = 2

    for j in range(n - 2, 0, -1): 
        i = j - 1
        k = j + 1
        while(i >= 0 and k <= n - 1): 
            if (set[i] + set[k] < 2 * set[j]): 
                k += 1
  
            elif (set[i] + set[k] > 2 * set[j]): 
                L[i][j] = 2
                i -= 1
            else:  
                L[i][j] = L[j][k] + 1 
                llap = max(llap, L[i][j]) 
                i -= 1
                k += 1
                while (i >= 0): 
                    L[i][j] = 2
                    i -= 1
    return llap 

if __name__ == "__main__": 
    n1 = int(input())
    set1 = list(map(int,input().strip().split()))
    print(lenghtOfLongestAP(set1, n1)) 
#-----------------------------METHOD3---------------------------------#
def Solve(A,n):  
    if n<=2 :  
        return n  
    llap = [2]*n  
	ans = 2
    for j in range(n-2, -1, -1):  
        i= j-1
        k= j+1
        while(i>=0 and k<n):  
            if A[i]+A[k] == 2*A[j]:  
                llap[j] = max(llap[k]+1,llap[j])  
                ans = max(ans, llap[j])  
                i-=1
                k+=1
            elif A[i]+A[k] < 2*A[j]:  
                k += 1
            else:  
                i -= 1
    return ans   

if __name__ == "__main__": 
    n1 = int(input())
    set1 = list(map(int,input().strip().split()))
    print(Solve(set1, n1)) 
