def findOddPair(A, N) : 
  
    count = 0
  
    # find all pairs  
    for i in range(0 , N) :  
        if (A[i] % 2 == 0) : 
            count+=1
      
    # return number of odd-even pair  
    return count * (N - count)  
  
# Driver Code 
if __name__=='__main__': 
    a = [5, 4, 7, 2, 1]  
    n = len(a) 
    print(findOddPair(a,n)) 
