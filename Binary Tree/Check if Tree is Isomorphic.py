def isIsomorphic(n1, n2): 
    #code here.
    if not n1 and not n2:
        return True
    if not n1 or not n2:
        return False
    if n1.data!=n2.data:
        return False
    return (isIsomorphic(n1.left,n2.left) and isIsomorphic(n1.right,n2.right)) or (isIsomorphic(n1.left,n2.right) and isIsomorphic(n1.right,n2.left))
