#----------Normal gcd------------#
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

t = int(input())
for cases in range(t):
    n = int(input())
    res = 0
    for i in range(1,n):
        if gcd(n,i)==1:
            res+=1
    print(res)
#--------Euler Totient Function-------------#
def phi(n):
    res = n
    p = 2
    while p*p <= n:
        if n%p==0:
            while n%p==0:
                n = n//p
            res -= res//p
        p+=1
    
    if n>1:
        res -= res//n
    return res

t = int(input())
for cases in range(t):
    n = int(input())
    print(phi(n))
