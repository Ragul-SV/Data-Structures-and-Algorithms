#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    p = s[:]
    l = 0
    r = n-1
    while l<=r:
        if s[l]!=s[r]:
            p[l] = p[r] = max(s[l],s[r])
            k-=1
        l+=1
        r-=1
        
    
    if k<0:
        return str(-1)
    l = 0
    r = n-1
    while l<=r:
        if l==r and k>0:
            p[l] = '9'
        if p[l]<'9':
            if k>=2 and p[l]==s[l] and p[r]==s[r]:
                p[l] = p[r] = '9'
                k-=2
            elif k>=1 and (p[l]!=s[l] or p[r]!=s[r]):
                p[l] = p[r] = '9'
                k-=1
        l+=1
        r-=1
    return "".join(p)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()
    s = [i for i in s]
    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
