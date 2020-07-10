def findEvenPair(A, N): 
    count = 0
   
    # find all pairs 
    for i in range(0,N): 
        if (A[i] % 2 != 0): 
            count+=1
   
    totalPairs = (N * (N - 1) / 2) 
    oddEvenPairs = count * (N - count) 
   
    # return number of even pair 
    return (int)(totalPairs - oddEvenPairs) 
  
# Driver Code 
def main(): 
    a = [ 5, 4, 7, 2, 1 ] 
    n = len(a) 
   
    # calling function findEvenPair 
    # and pr number of even pair 
    print(findEvenPair(a, n)) 
   
if __name__ == '__main__': 
    main() 
