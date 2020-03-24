def post(root,sum):
    if not root:
        return 0
    lsum = post(root.left,sum)
    rsum = post(root.right,sum)
    sum[0] += abs(lsum-rsum)
    return lsum+rsum+root.data

def tiltTree(root):
    sum = [0]
    post(root,sum)
    return sum[0]
