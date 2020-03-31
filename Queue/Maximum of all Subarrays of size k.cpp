#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,n,k,i;
	cin>>t;
	while(t--)
	{
	    cin>>n>>k;
	    int arr[n];
	    for(i=0;i<n;i++)
	    {
	        cin>>arr[i];
	    }
	    deque<int> q;
	    for(i=0;i<k;i++)
	    {
	        while(!q.empty() and arr[i]>=arr[q.back()])
	            q.pop_back();
	        q.push_back(i);
	    }
	    for(;i<n;i++)
	    {
	        cout<<arr[q.front()]<<" ";
	        while(!q.empty() and q.front()<=i-k)
	            q.pop_front();
	        while(!q.empty() and arr[i]>=arr[q.back()])
	            q.pop_back();
	        q.push_back(i);
	    }
	    cout<<arr[q.front()]<<endl;
	}
	return 0;
}
