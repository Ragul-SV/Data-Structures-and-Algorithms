class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val
        self.elecount = 1
        self.lcount = 0

def insertBST(root,curnode):
    c = 0
    while root!=None:
        prev = root
        if curnode.data>root.data:
            c += root.elecount+root.lcount
            root = root.right
        elif curnode.data<root.data:
            root.lcount+=1
            root = root.left
        else:
            prev = root
            prev.elecount+=1
            break
    if curnode.data<prev.data:
        prev.left = curnode
    elif curnode.data>prev.data:
        prev.right = curnode
    else:
        return c+prev.lcount
    return c
    
def constructBST(arr,n):
    root = Node(arr[-1])
    res = [0]
    for i in range(n-2,-1,-1):
        res.append(insertBST(root,Node(arr[i])))
    return res[::-1]

t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = constructBST(arr,n)
    for i in range(n):
        print(res[i],end=" ")
    print()
