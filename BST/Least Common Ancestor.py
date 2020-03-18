def ancestor(root,n1,n2):
    if not root:
        return None
    if root.key>n1 and root.key>n2:
        return ancestor(root.left,n1,n2)
    if root.key<n1 and root.key<n2:
        return ancestor(root.right,n1,n2)
    return root.key
 
 
def LCA(root,n1,n2):
    '''
    :param root: given root of the bst
    :param n1: value one.
    :param n2: value two.
    :return: Lowest common Ancestor key.
    '''
    if n1>n2:
        n1,n2 = n2,n1
    return ancestor(root,n1,n2)
