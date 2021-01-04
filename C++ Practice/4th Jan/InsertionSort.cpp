#include <bits/stdc++.h>
using namespace std;

int main() {
	int arr[10] = {25,46,51,72,81,34,11,2,86,44};
	int n = sizeof(arr)/sizeof(arr[0]);
	int j,temp;
	for(int i=1;i<n;i++)
	{
		j = i-1;
		temp = arr[i];
		while(j>=0 && temp<arr[j])
		{
			arr[j+1] = arr[j];
			j--;
		}
		arr[j+1] = temp;
	}
	
	for(int i=0;i<n;i++)
	cout<<arr[i]<<" ";
	cout<<endl;
	return 0;
}
