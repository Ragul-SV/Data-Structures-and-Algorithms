#include <bits/stdc++.h> 
using namespace std; 

// Function to permute the the given 
// array based on the given conditions 
int permute(int A[], int P[], int n) 
{ 
	// For each element of P 
	int nxt;
  	for(int i=0;i<n;i++)
    {
      nxt = i;
      while(P[nxt]>=0)
      {
        int temp = P[nxt];
        swap(A[i],A[P[nxt]]);
        P[nxt] -= n;
        nxt = temp;
      }
    }
} 

// Driver code 
int main() 
{ 
	int A[] = { 5, 6, 7, 8 }; 
	int P[] = { 3, 2, 0, 1 }; 
	int n = sizeof(A) / sizeof(int); 

	permute(A, P, n); 

	// Print the new array after 
	// applying the permutation 
	for (int i = 0; i < n; i++) 
		cout << A[i] << " "; 

	return 0; 
} 
