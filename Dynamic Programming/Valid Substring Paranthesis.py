#---------------------------------------------------O(n^3)---------------------------------------------------------------------#
def isValid(s):
    q = []
    for i in range(len(s)):
        if s[i]=='(':
            q.append(s[i])
        elif q and q[-1]=='(':
            q.pop()
        else: 
            return False
    return len(q)==0

t = int(input())
for cases in range(t):
    s = input()
    n = len(s)
    maxlen = 0
    for i in range(n):
        for j in range(i+2,n+1,2):
            if(isValid(s[i:j])):
                maxlen = max(maxlen,j-i)
    print(maxlen)

#--------------------------------------------------O(n)----------------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    s = input()
    n = len(s)
    dp = [0]*n
    maxlen = 0
    for i in range(1,n):
        if s[i]==')':
            if s[i-1]=='(':
                if i>=2:
                    dp[i] = dp[i-2] + 2
                else:
                    dp[i] = 2
            elif i-dp[i-1]>=1 and s[i-dp[i-1]-1]=='(':
                if i-dp[i-1]>=2:
                    dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2
                else:
                    dp[i] = dp[i-1] + 2
        maxlen = max(maxlen,dp[i])
    print(maxlen)
