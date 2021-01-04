#include <bits/stdc++.h>
using namespace std;

void swap(int &a,int &b)
{
	int temp = a;
	a = b;
	b = temp;
}

int partition(int arr[],int low,int high)
{
	int pivot = arr[high];
	int i=low;
	for(int j=low;j<high;j++)
	{
		if(arr[j]<pivot)
		{
			swap(arr[j],arr[i]);
			i++;
		}
	}
	swap(arr[i],arr[high]);
	return i;
}

void quickSort(int arr[],int low,int high)
{
	if(low<high)
	{
		int p = partition(arr,low,high);
		quickSort(arr,low,p-1);
		quickSort(arr,p+1,high);
	}
}

int main() {
	int arr[10] = {25,46,51,72,81,34,11,2,86,44};
	int n = sizeof(arr)/sizeof(arr[0]);
	quickSort(arr,0,n-1);
	for(int i=0;i<n;i++)
	cout<<arr[i]<<" ";
	cout<<endl;
	return 0;
}
