#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ll;
int main() {
	ll t,n,k,i,flag,temp;
	cin>>t;
	while(t--)
	{
	    cin>>n>>k;
	    unordered_set<ll> s;
	    flag = 0;
	    for(i=0;i<n;i++)
	    {
	        cin>>temp;
	        if(!flag)
	        {
	            if(temp>0 and k%temp==0 and s.count(k/temp))
	            {
	                cout<<"Yes"<<endl;
	                flag = 1;
	            }
	            s.insert(temp);
	        }
	    }
	    if(!flag) cout<<"No"<<endl;
	}
	return 0;
}
