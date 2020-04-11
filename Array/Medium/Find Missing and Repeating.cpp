#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,n,i,min;
	cin>>t;
	while(t--)
	{
	    cin>>n;
	    int arr[n];
	    min = INT_MAX;
	    for(i=0;i<n;i++)
	    {
	        cin>>arr[i];
	    }
	    for(i=0;i<n;i++)
	    {
	        if(arr[abs(arr[i])-1]>0) arr[abs(arr[i])-1]*=-1;
	        else if(abs(arr[i])<min) min = abs(arr[i]);
	    }
	    cout<<min<<" ";
	    for(i=0;i<n;i++)
	    {
	        if(arr[i]>0)
	        {
	            cout<<i+1<<endl;
	            break;
	        }
	    }
	}
	return 0;
}
