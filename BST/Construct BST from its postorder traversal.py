#-----------------------------------------O(N)--------------------------------------------#
INT_MIN = -2**31
INT_MAX = 2**31
 
class newNode:  
    def __init__(self, data):  
        self.data = data  
        self.left = self.right = None
 
def constructTreeUtil(post, postIndex,  
                      key, min, max, size):  
 
    if (postIndex[0] < 0): 
        return None
 
    root = None
 
    if (key > min and key < max) : 
 
        root = newNode(key)  
        postIndex[0] = postIndex[0] - 1
 
        if (postIndex[0] >= 0) : 
 
            root.right = constructTreeUtil(post, postIndex, 
                                           post[postIndex[0]],  
                                           key, max, size )  
 
            root.left = constructTreeUtil(post, postIndex, 
                                          post[postIndex[0]],  
                                          min, key, size )  
 
    return root  
 
def constructTree (post, size) : 
 
    postIndex = [size-1] 
    return constructTreeUtil(post, postIndex,  
                             post[postIndex[0]], 
                             INT_MIN, INT_MAX, size)  
 
def printInorder (node) : 
 
    if (node == None) : 
        return
    printInorder(node.left)  
    print(node.data, end = " ")  
    printInorder(node.right)  
 
if __name__ == '__main__': 
    post = [1, 7, 5, 50, 40, 10] 
    size = len(post)  
 
    root = constructTree(post, size)  
 
    print("Inorder traversal of the constructed tree: ")  
    printInorder(root) 
 
