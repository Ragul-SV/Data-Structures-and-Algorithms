def diagonalSum(root):
    s = []
    s.append(root)
    while s:
        sum = 0
        size = len(s)
        for _ in range(size):
            temp = s.pop(0)
            while temp:
                if temp.left:
                    s.append(temp.left)
                sum+=temp.data
                temp = temp.right
        print(sum,end=" ")
