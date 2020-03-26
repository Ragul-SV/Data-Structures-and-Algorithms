def serialize(root, A):
    if not root:
        A.append(-1)
        return
    A.append(root.data)
    serialize(root.left,A)
    serialize(root.right,A)
    
def deserialize(arr,i):
    if i[0]==len(arr) or arr[i[0]]==-1:
        i[0]+=1
        return None
    root = Node(arr[i[0]])
    i[0]+=1
    root.left = deserialize(arr,i)
    root.right = deserialize(arr,i)
    return root
    
def deSerialize(A):
    i = [0]
    return deserialize(A,i)
