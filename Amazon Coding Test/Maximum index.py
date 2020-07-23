def maxIndex(steps, badIndex):
    i,j = 0,1
    s = steps
    while steps>0:
        if i+j != badIndex:
            i = i+j
        steps-=1
        j+=1
    i1,j = 0,2
    steps = s-1
    while steps>0:
        if i1+j != badIndex:
            i1 = i1+j
        steps-=1
        j+=1
    return max(i,i1)
