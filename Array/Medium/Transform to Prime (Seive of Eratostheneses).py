#-------------------------------------METHOD1-----O(N)---------------------------------------#
isPrime = [True]*100001

def seiveOfEratostheneses():
    isPrime[1] = False
    i = 2
    while i*i<100001:
        if isPrime[i]:
            j = i*2
            while j<100001:
                isPrime[j] = False
                j+=i
        i+=1
        
def findNextPrime(n):
    n = n+1
    while n:
        if isPrime[n]:
            return n
        n+=1
        
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    s = sum(arr)
    seiveOfEratostheneses()
    if isPrime[s]:
        print(0)
    else:
        n = findNextPrime(s)
        print(n-s)
#------------------------------------METHOD2--------O(N*LOG(LOGN))-------------------------------#
import math
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def findNextPrime(n):
    n = n+1
    while n:
        if isPrime(n):
            return n
        n+=1

t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    s = sum(arr)
    if isPrime(s):
        print(0)
    else:
        n = findNextPrime(s)
        print(n-s)
