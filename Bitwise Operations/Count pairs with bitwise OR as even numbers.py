def findEvenPair(A, N): 
  
    # Count total even numbers  
    # in array. 
    count = 0
    for i in range(N):  
        if (not (A[i] & 1)): 
            count += 1
            
    # return count of even pair 
    return count * (count - 1) // 2
  
# Driver Code 
if __name__ == "__main__": 
    A = [ 5, 6, 2, 8 ] 
    N = len(A) 
    print(findEvenPair(A, N)) 
