def reverseInorder(root,s):
    if root:
        reverseInorder(root.right,s)
        root.data = s[0] + root.data
        s[0] = root.data
        reverseInorder(root.left,s)
 
def modifyBST(root):
    # Code here
    s = [0]
    reverseInorder(root,s)
