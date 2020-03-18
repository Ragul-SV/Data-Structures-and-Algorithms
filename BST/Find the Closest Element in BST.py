def mindif(root,k,d):
    if root:
        tmp = abs(root.key - k)
        d[0] = min(tmp,d[0])
        if k<root.key:
            mindif(root.left,k,d)
        else:
            mindif(root.right,k,d)
    else:
        return
 
 
def maxDiff(root, k):
    '''
    :param root: given root of bst
    :param k: value of k
    :return: Integer, minimum absolute difference possible
    '''
    # code here
    d = [1000000]
    mindif(root,k,d)
    return d[0]
