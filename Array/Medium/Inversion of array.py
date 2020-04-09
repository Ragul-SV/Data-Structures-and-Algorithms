def mergeSort(arr,temp,l,r):
	if l<r:
		mid = (l+r)//2
		mergeSort(arr,temp,l,mid)
		mergeSort(arr,temp,mid+1,r)
		merge(arr,temp,l,mid,r)
		
def merge(arr,temp,l,mid,r):
	i = l
	j = mid+1
	k = l
	while i<=mid and j<=r:
		if arr[i]<=arr[j]:
			temp[k]=arr[i]
			i+=1
		else:
			temp[k]=arr[j]
			j+=1
		k+=1
	while i<=mid:
		temp[k]=arr[i]
		k+=1
		i+=1
	while j<=r:
		temp[k]=arr[j]
		k+=1
		j+=1
	for i in range(l,r+1):
		arr[i] = temp[i]

t = int(input())
for cases in range(t):
	n = int(input())
	arr = list(map(int,input().strip().split()))
	temp = [0]*n
	mergeSort(arr,temp,0,n-1)
	print(arr)
