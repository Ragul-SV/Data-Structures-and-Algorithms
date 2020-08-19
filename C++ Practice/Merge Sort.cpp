#include <bits/stdc++.h>
using namespace std;

void merge(int arr[],int l,int mid,int r,int temp[])
{
	int k = l;
	int i = l,j = mid+1;
	while(i<=mid && j<=r)
	{
		if(arr[i]<=arr[j])
		{
			temp[k] = arr[i];
			i++;
			k++;
		}
		else
		{
			temp[k] = arr[j];
			j++;
			k++;
		}
	}
	while(i<=mid)
	{
		temp[k] = arr[i];
		i++;
		k++;
	}
	while(j<=r)
	{
		temp[k] = arr[j];
		j++;
		k++;
	}
	for(int i=l;i<=r;i++)
	{
		arr[i] = temp[i];
	}
}

void mergeSort(int arr[],int l,int r,int temp[])
{
	if(l<r)
	{
		int mid = (l+r)/2;
		mergeSort(arr,l,mid,temp);
		mergeSort(arr,mid+1,r,temp);
		merge(arr,l,mid,r,temp);
	}
}

int main() {
	int n;
	int arr[] = {12,4,84,35,2,75};
	n = sizeof(arr)/sizeof(arr[0]);
	int temp[n+1] = {0};
	mergeSort(arr,0,n,temp);
	for(int i=0;i<n;i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;
	return 0;
}
