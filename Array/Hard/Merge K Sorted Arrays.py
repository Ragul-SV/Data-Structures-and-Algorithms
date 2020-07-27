class HeapNode:
    def __init__(self,data,i,j):
        self.data = data
        self.i = i  #index of array from which the element is taken
        self.j = j  #index of next element in the array
    
class Heap:
    def __init__(self,arr,n):
        self.heap = arr
        self.size = n
        i = (n-1)//2
        while i>=0:
            self.min_heapify(i)
            i-=1
    
    def min_heapify(self,i):
        l = 2*i+1
        r = 2*i+2
        small = i
        if l<self.size and self.heap[l].data<self.heap[i].data:
            small = l
        if r<self.size and self.heap[r].data<self.heap[small].data:
            small = r
        if small!=i:
            self.heap[small],self.heap[i] = self.heap[i],self.heap[small]
            self.min_heapify(small)
            
def mergeKArrays(arr,n):
    res_size = 0
    h_arr = []
    for i in range(n):
        node = HeapNode(arr[i][0],i,1)
        h_arr.append(node)
        res_size+=len(arr[i])
    min_heap = Heap(h_arr,n)
    res = [0]*res_size
    for i in range(res_size):
        root = min_heap.heap[0]
        res[i] = root.data
        if root.j<len(arr[root.i]):
            root.data = arr[root.i][root.j]
            root.j+=1
        else:
            root.data = 2**31
        min_heap.heap[0] = root
        min_heap.min_heapify(0)
    return res
