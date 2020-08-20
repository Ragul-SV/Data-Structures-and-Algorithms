#include <bits/stdc++.h>
using namespace std;

int printFirstRepeating(int arr[],int n)
{
	unordered_map<int,int> mp;
	int index = n+1;
	for(int i=0;i<n;i++)
	{
		if(mp.find(arr[i])!=mp.end()) index = min(index,mp[arr[i]]);
		else mp[arr[i]] = i;
	}
	if(index!=n+1) return arr[index];
	else return -1;
}

int main() {
	int arr[] = {10, 5, 3, 4, 3, 5, 6}; 
  
    int n = sizeof(arr) / sizeof(arr[0]); 
    cout<<printFirstRepeating(arr, n);
    return 0;
}
