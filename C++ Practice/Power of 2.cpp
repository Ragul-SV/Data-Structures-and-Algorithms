#include<bits/stdc++.h> 
using namespace std; 
  
bool isPowerOfTwo(int n) 
{ 
   if(n==0) 
   return false; 
 
   return (ceil(log2(n)) == floor(log2(n))); 
} 
  
int main() 
{ 
    isPowerOfTwo(31)? cout<<"Yes"<<endl: cout<<"No"<<endl; 
    isPowerOfTwo(64)? cout<<"Yes"<<endl: cout<<"No"<<endl; 
  
    return 0; 
} 

//------------------------------------------------------------------------------------------------------------------------------------
#include <bits/stdc++.h> 
using namespace std; 
#define bool int  
  
bool isPowerOfTwo (int x)  
{  
    return x && (!(x&(x-1)));  
}  
  
int main()  
{  
    isPowerOfTwo(31)? cout<<"Yes\n": cout<<"No\n";  
    isPowerOfTwo(64)? cout<<"Yes\n": cout<<"No\n";  
    return 0;  
}  
