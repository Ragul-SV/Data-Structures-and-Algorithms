#include <bits/stdc++.h>
using namespace std;

int main() {
	int arr[4] = {-6,-3,-7,-2};
	int n = sizeof(arr)/sizeof(arr[0]);
	vector<int> vec;
	for(int i=n-1;i>=0;i--)
	{
		int ls = 0,rs=0;
		if(vec.empty()){vec.push_back(arr[i]);arr[i] = 0;}
		else if(vec.size()==1){if(arr[i]>vec[0])vec.push_back(arr[i]);else vec.insert(vec.begin(),arr[i]);
		arr[i] = 0;}
		else{
		for(int j=0;j<vec.size()-1;j++)
		{
			if(arr[i]<vec[j]){vec.insert(vec.begin()+j,arr[i]);arr[i] = 0;break;}
			if(j==vec.size()-2 && arr[i]>vec[j] && arr[i]>vec[j+1]){vec.push_back(arr[i]);arr[i] = 0;break;}
			else if(vec[j]<arr[i] && arr[i]<vec[j+1])
			{
				ls+=vec[j];
				for(int k=j+1;k<vec.size();k++){rs+=vec[k];}
				vec.insert(vec.begin()+j+1,arr[i]);
				arr[i]=ls*rs;
				break;
			}
			else if(vec[j]<arr[i] && vec[j+1]<arr[i])
			{
				ls+=vec[j];
			}
		}}
	}
	for(int i=0;i<n;i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;
	return 0;
}
