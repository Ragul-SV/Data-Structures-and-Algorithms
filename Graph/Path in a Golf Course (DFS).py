def check(a,r,c,n):
    if r==n-1 and c==n-1:
        return 1
    if a[r][c]==0:
        return 0
    m = a[r][c]
    a[r][c] = 0
    for i in range(m,-1,-1):
        if (r+i)<n:
            if check(a,r+i,c,n):
                return 1
        if (c+i)<n:
            if check(a,r,c+i,n):
                return 1
        if r-i >= 0:
            if check(a,r-i,c,n):
                return 1
        if c-i>=0:
            if check(a,r,c-i,n):
                return 1
    return 0

def is_possible(a,n):
    return check(a,0,0,n)
