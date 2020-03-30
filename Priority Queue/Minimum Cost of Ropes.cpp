#include<bits/stdc++.h>

using namespace std;
int main()
 {
	int t,temp;
	cin >> t;
	while(t--)
	{
	    int n;
	    cin >> n;
	    vector<int> vec;
	    priority_queue<int,vector<int>,greater<int>> pq;
	    for(int i=0;i<n;i++)
	    {
	        cin>>temp;
	        pq.push(temp);
	    }
	    long sum = 0;
	    
	    while(pq.size()>1)
	    {
	        int min1 = pq.top();
	        pq.pop();
	        int min2 = pq.top();
	        pq.pop();
	        
	        int min = min1+min2;
	        sum+=min;
	        pq.push(min);
	   }
	   cout << sum << endl;
	}
}
