def tour(lis, n):
    capacity = 0
    deficit = 0
    start = 0
    for i in range(n):
        capacity += lis[i][0] - lis[i][1]
        if capacity<0:
            deficit += capacity
            capacity = 0
            start = i+1
    if capacity+deficit>=0:
        return start
    else:
        return -1
