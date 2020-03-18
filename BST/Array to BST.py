def buildBST(arr,start,end):
    if start>end:
        return 
    mid = (start+end)//2
    temp = Node(arr[mid])
    temp.left = buildBST(arr,start,mid-1)
    temp.right = buildBST(arr,mid+1,end)
    return temp
 
def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
 
class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        arr.sort()
        temp = buildBST(arr,0,n-1)
        preorder(temp)
        print()
